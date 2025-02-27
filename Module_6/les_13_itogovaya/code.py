import telebot
import datetime
import sqlite3
from pathlib import Path

TOKEN = '8063391832:AAGlsqsWs1ODOE2fznIERykoxVfPmi3JwFM'
CURRENT_FILE = Path(__file__).resolve()
BASE_DIR = CURRENT_FILE.parent
SQL_BASE = BASE_DIR / 'sleep_data.db'

# Инициализация бота
bot = telebot.TeleBot(TOKEN)

# Подключение к базе данных SQLite
conn = sqlite3.connect(SQL_BASE, check_same_thread=False)
cursor = conn.cursor()

# Создание таблиц, если они не существуют
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT
)''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS sleep_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    sleep_time DATETIME,
    wake_time DATETIME,
    sleep_quality INTEGER,
    FOREIGN KEY(user_id) REFERENCES users(id)
)''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT,
    sleep_record_id INTEGER,
    FOREIGN KEY(sleep_record_id) REFERENCES sleep_records(id)
)''')
conn.commit()

# Функция для сохранения данных пользователя
def save_user(user_id, name):
    cursor.execute('''
    INSERT OR IGNORE INTO users (id, name)
    VALUES (?, ?)''', (user_id, name))
    conn.commit()

# Функция для сохранения данных сна
def save_sleep_data(user_id, sleep_time, wake_time, sleep_quality):
    cursor.execute('''
    INSERT INTO sleep_records (user_id, sleep_time, wake_time, sleep_quality)
    VALUES (?, ?, ?, ?)''', (user_id, sleep_time, wake_time, sleep_quality))
    conn.commit()
    return cursor.lastrowid

# Функция для добавления заметки к записи о сне
def add_note(sleep_record_id, text):
    cursor.execute('''
    INSERT INTO notes (text, sleep_record_id)
    VALUES (?, ?)''', (text, sleep_record_id))
    conn.commit()

# Функция для загрузки времени начала сна
def load_sleep_data(user_id):
    cursor.execute('''
    SELECT sleep_time FROM sleep_records 
    WHERE user_id = ? 
    ORDER BY id DESC LIMIT 1''', (user_id,))
    result = cursor.fetchone()
    return result[0] if result else None

# Основная функция для обработки команды /start
@bot.message_handler(commands=['start'])
def start_command(message):
    user_id = message.from_user.id
    name = message.from_user.first_name
    save_user(user_id, name)
    chat_id = message.chat.id
    bot.send_message(chat_id, "Привет! Я бот для отслеживания сна. Используй команды /sleep и /wake.")

# Основная функция для обработки команды /sleep
@bot.message_handler(commands=['sleep'])
def sleep_command(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    sleep_time = datetime.datetime.now()
    bot.send_message(chat_id, "Отправляйся спать. Утром сообщи, когда проснёшься.")

# Основная функция для обработки команды /wake
@bot.message_handler(commands=['wake'])
def wake_command(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    wake_time = datetime.datetime.now()
    
    # Получаем качество сна из сообщения
    try:
        sleep_quality = int(message.text.split(maxsplit=1)[1])
    except (IndexError, ValueError):
        sleep_quality = 0

    # Проверка, была ли команда /sleep вызвана ранее
    start_time = load_sleep_data(user_id)
    if start_time is None:
        bot.send_message(chat_id, "Не удалось определить начало сна. Используй /sleep перед /wake.")
        return

    # Сохранение записи о сне
    sleep_record_id = save_sleep_data(user_id, start_time, wake_time, sleep_quality)

    # Добавление заметки, если она предоставлена
    try:
        notes = message.text.split(maxsplit=1)[1]
        add_note(sleep_record_id, notes)
    except IndexError:
        pass

    # Расчет длительности сна
    duration = wake_time - datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
    duration_in_seconds = duration.total_seconds()
    hours = int(duration_in_seconds // 3600)
    minutes = int((duration_in_seconds % 3600) // 60)

    # Форматированный ответ пользователю
    response = f"Ты спал {hours} часов и {minutes} минут\n"
    response += f"Качество сна: {sleep_quality}/10\n"

    if sleep_quality >= 8:
        response += "Отлично! Продолжай в том же духе 😊"
    elif sleep_quality >= 5:
        response += "Неплохо, но можно лучше 😉"
    else:
        response += "Похоже, нужно поработать над качеством сна 😴"

    bot.send_message(chat_id, response)

# Функция для получения статистики
@bot.message_handler(commands='stats')
def stats_command(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    
    # Получаем все записи сна пользователя
    cursor.execute('''
    SELECT sleep_time, wake_time, sleep_quality 
    FROM sleep_records 
    WHERE user_id = ? 
    ORDER BY sleep_time DESC LIMIT 7''', (user_id,))
    
    records = cursor.fetchall()
    if not records:
        bot.send_message(chat_id, "У тебя пока нет записей сна.")
        return
    
    # Подготавливаем статистику
    total_sleep = datetime.timedelta()
    quality_sum = 0
    sleep_log = []
    
    for record in records:
        sleep_time = datetime.datetime.strptime(record[0], '%Y-%m-%d %H:%M:%S')
        wake_time = datetime.datetime.strptime(record[1], '%Y-%m-%d %H:%M:%S')
        quality = record[2]
        
        duration = wake_time - sleep_time
        total_sleep += duration
        quality_sum += quality
        
        sleep_log.append(f"{sleep_time.strftime('%d.%m')} {sleep_time.strftime('%H:%M')} - {wake_time.strftime('%H:%M')}: {quality}/10")
    
    # Расчет средних значений
    average_sleep = total_sleep / len(records)
    average_quality = quality_sum / len(records)
    
    # Форматированный ответ со статистикой
    stats_message = f"Статистика за последние 7 дней:\n\n"
    stats_message += f"Средняя продолжительность сна: {int(average_sleep.total_seconds() // 3600)} часов\n"
    stats_message += f"Среднее качество сна: {average_quality:.1f}/10\n\n"
    stats_message += "Журнал сна:\n"
    stats_message += "\n".join(sleep_log)
    
    bot.send_message(chat_id, stats_message)

# Запуск бота
if __name__ == '__main__':
    bot.polling(none_stop=True)