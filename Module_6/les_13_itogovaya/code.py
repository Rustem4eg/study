import telebot
from datetime import datetime
import sqlite3
from pathlib import Path
from telebot import types

TOKEN = '8063391832:AAGlsqsWs1ODOE2fznIERykoxVfPmi3JwFM'
CURRENT_FILE = Path(__file__).resolve()
BASE_DIR = CURRENT_FILE.parent
SQL_BASE = BASE_DIR / 'sleep_data.db'

user_status = {}

bot = telebot.TeleBot(TOKEN)

# Подключение к базе данных SQLite
conn = sqlite3.connect(SQL_BASE, check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS sleep_data (
 id INTEGER PRIMARY KEY,
 user_id INTEGER,
 start_sleep TEXT,
 stop_sleep TEXT,
 duration TEXT,
 sleep_mark INTEGER,
 note TEXT
)''')
conn.close()

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Привет, я бот Морфей. Я отслеживаю твой сон. Когда будешь ложиться спать, нажми /sleep')

@bot.message_handler(commands=['sleep'])
def start_sleep(message):
    user_id = message.from_user.id
    
    if user_id in user_status and user_status.get(user_id) == 'sleeping':
        bot.reply_to(message, 'Кажется, ты уже отмечал начало сна. Не нужно повторять команду.')
        return
    
    start_time = datetime.now()
    
    conn = sqlite3.connect(SQL_BASE)
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO sleep_data (user_id, start_sleep) VALUES (?, ?)',
        (user_id, start_time.strftime('%Y-%m-%d %H:%M:%S'))
    )
    conn.commit()
    conn.close()
    
    user_status[user_id] = 'sleeping'
    bot.reply_to(message, 'Начало сна зафиксировано. Нажми /wake, когда проснёшься')

@bot.message_handler(commands=['wake'])
def wake_up(message):
    user_id = message.from_user.id
    
    if user_id not in user_status or user_status.get(user_id) != 'sleeping':
        bot.reply_to(message, 'Кажется, ты не отмечал начало сна. Сначала нажми /sleep.')
        return
    
    stop_time = datetime.now()
    
    conn = sqlite3.connect(SQL_BASE)
    cursor = conn.cursor()
    cursor.execute(
        'SELECT start_sleep, id FROM sleep_data WHERE user_id = ? ORDER BY id DESC LIMIT 1',
        (user_id,)
    )
    result = cursor.fetchone()
    
    if result:
        start_sleep = datetime.strptime(result[0], '%Y-%m-%d %H:%M:%S')
        duration = stop_time - start_sleep
        duration_str = str(duration).split('.')[0]
        last_id = result[1]
        
        cursor.execute(
            'UPDATE sleep_data SET stop_sleep = ?, duration = ? WHERE id = ?',
            (stop_time.strftime('%Y-%m-%d %H:%M:%S'), duration_str, last_id)
        )
        conn.commit()
        conn.close()
        
        user_status[user_id] = 'awake'
        bot.reply_to(message, f'Конец сна зафиксирован!\n'
                            f'Начало: {start_sleep.strftime("%H:%M")}\n'
                            f'Конец: {stop_time.strftime("%H:%M")}\n'
                            f'Продолжительность: {duration_str}')

@bot.message_handler(commands=['rate'])
def rate_sleep(message):
    user_id = message.from_user.id
    if user_id not in user_status or user_status.get(user_id) != 'awake':
     bot.reply_to(message, 'Сначала отметь пробуждение командой /wake')
     return
 
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    for i in range(1, 6):
     keyboard.add(str(i))
 
    msg = bot.send_message(message.chat.id, 'Оцени качество сна от 1 до 5:', reply_markup=keyboard)
    bot.register_next_step_handler(msg, set_sleep_mark)

def set_sleep_mark(message):
    try:
        user_id = message.from_user.id
        mark = int(message.text)

        if not 1 <= mark <= 5:
            raise ValueError

        conn = sqlite3.connect(SQL_BASE)
        cursor = conn.cursor()
        cursor.execute(
            'UPDATE sleep_data SET sleep_mark = ? WHERE user_id = ? AND id = (SELECT max(id) FROM sleep_data WHERE user_id = ?)',
            (mark, user_id, user_id)
        )
        conn.commit()
        conn.close()

        bot.reply_to(message, f'Оценка сна: {mark} баллов. Хочешь добавить заметку? (/note)')

    except ValueError:
        bot.reply_to(message, 'Пожалуйста, выбери число от 1 до 5.')

@bot.message_handler(commands=['note'])
def add_note(message):
    user_id = message.from_user.id

    if user_id not in user_status or user_status.get(user_id) != 'awake':
        bot.reply_to(message, 'Сначала отметь пробуждение командой /wake')
        return

    msg = bot.send_message(message.chat.id, 'Напиши заметку о сне:')
    bot.register_next_step_handler(msg, set_note)

def set_note(message):
    user_id = message.from_user.id
    note = message.text

    conn = sqlite3.connect(SQL_BASE)
    cursor = conn.cursor()
    cursor.execute(
        'UPDATE sleep_data SET note = ? WHERE user_id = ? AND id = (SELECT max(id) FROM sleep_data WHERE user_id = ?)',
        (note, user_id, user_id)
    )
    conn.commit()
    conn.close()

    bot.reply_to(message, 'Заметка добавлена!')
    user_status[user_id] = 'logged'

@bot.message_handler(commands=['stats'])
def show_stats(message):
    user_id = message.from_user.id

    conn = sqlite3.connect(SQL_BASE)
    cursor = conn.cursor()
    cursor.execute(
        'SELECT start_sleep, stop_sleep, duration, sleep_mark, note FROM sleep_data WHERE user_id = ? ORDER BY id DESC LIMIT 5',
        (user_id,)
    )
    results = cursor.fetchall()
    conn.close()

    if not results:
        bot.reply_to(message, 'Нет данных для отображения.')
        return

    stats_message = 'Последние 5 записей:\n\n'
    for i, row in enumerate(results):
        stats_message += f'Запись {i+1}:\n'
        stats_message += f'Начало: {row[0]}\n'
        stats_message += f'Конец: {row[1]}\n'
        stats_message += f'Продолжительность: {row[2]}\n'
        stats_message += f'Оценка: {row[3] or "еще не оценено"}\n'
        stats_message += f'Заметка: {row[4] or "нет заметки"}\n\n'

    bot.reply_to(message, stats_message)

if __name__ == '__main__':
    bot.polling(none_stop=True)