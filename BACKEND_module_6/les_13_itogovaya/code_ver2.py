import telebot
from datetime import datetime
import sqlite3
from pathlib import Path
from telebot import types
import os
from dotenv import load_dotenv


CURRENT_FILE = Path(__file__).resolve()
BASE_DIR = CURRENT_FILE.parent
SQL_BASE = BASE_DIR / 'sleep_data.db'
ENV_BASE = BASE_DIR / 'tg_bot.env'

if ENV_BASE.exists():
    load_dotenv(dotenv_path=ENV_BASE)
else:
    raise FileNotFoundError(f".env file not found at {ENV_BASE}")

TOKEN = os.getenv('TOKEN')
if TOKEN is None:
    raise ValueError("TOKEN variable is not set. Please add it to .env file")

bot = telebot.TeleBot(TOKEN)

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

def get_user_status(user_id):
    conn = sqlite3.connect(SQL_BASE)
    cursor = conn.cursor()
    cursor.execute(
        'SELECT id FROM sleep_data WHERE user_id = ? AND stop_sleep IS NULL',
        (user_id,)
    )
    result = cursor.fetchone()
    conn.close()
    
    return 'sleeping' if result else 'awake'

def set_user_status(user_id, status):
    conn = sqlite3.connect(SQL_BASE)
    cursor = conn.cursor()
    if status == 'sleeping':
        cursor.execute(
            'INSERT INTO sleep_data (user_id, start_sleep) VALUES (?, ?)',
            (user_id, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        )
    elif status == 'awake':
        cursor.execute(
            'UPDATE sleep_data SET stop_sleep = ? WHERE user_id = ? AND stop_sleep IS NULL',
            (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), user_id)
        )
    conn.commit()
    conn.close()

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Привет, я бот Морфей. Я отслеживаю твой сон. Когда будешь ложиться спать, нажми /sleep')

@bot.message_handler(commands=['sleep'])
def start_sleep(message):
    user_id = message.from_user.id
    
    if get_user_status(user_id) == 'sleeping':
        bot.reply_to(message, 'Кажется, ты уже отмечал начало сна. Не нужно повторять команду. Нажми /wake, чтобы зафиксировать пробуждение')
        return
    
    set_user_status(user_id, 'sleeping')
    bot.reply_to(message, 'Начало сна зафиксировано. Нажми /wake, когда проснёшься')

@bot.message_handler(commands=['wake'])
def wake_up(message):
    user_id = message.from_user.id
    
    if get_user_status(user_id) != 'sleeping':
        bot.reply_to(message, 'Кажется, ты не отмечал начало сна. Сначала нажми /sleep.')
        return
    
    conn = sqlite3.connect(SQL_BASE)
    cursor = conn.cursor()
    cursor.execute(
        'SELECT start_sleep, id FROM sleep_data WHERE user_id = ? AND stop_sleep IS NULL',
        (user_id,)
    )
    result = cursor.fetchone()
    
    if result:
        start_sleep = datetime.strptime(result[0], '%Y-%m-%d %H:%M:%S')
        stop_time = datetime.now()
        duration = stop_time - start_sleep
        duration_str = str(duration).split('.')[0]
        last_id = result[1]
        
        cursor.execute(
            'UPDATE sleep_data SET stop_sleep = ?, duration = ? WHERE id = ?',
            (stop_time.strftime('%Y-%m-%d %H:%M:%S'), duration_str, last_id)
        )
        conn.commit()
        conn.close()
        
        set_user_status(user_id, 'awake')
        bot.reply_to(message, f'Конец сна зафиксирован!\n'
                            f'Начало: {start_sleep.strftime("%H:%M")}\n'
                            f'Конец: {stop_time.strftime("%H:%M")}\n'
                            f'Продолжительность: {duration_str}\n'
                            f'Нажми /rate, чтобы оценить сон')

@bot.message_handler(commands=['rate'])
def rate_sleep(message):
    user_id = message.from_user.id
    
    conn = sqlite3.connect(SQL_BASE)
    cursor = conn.cursor()
    cursor.execute(
        'SELECT id FROM sleep_data WHERE user_id = ? AND stop_sleep IS NOT NULL AND sleep_mark IS NULL',
        (user_id,)
    )
    result = cursor.fetchone()
    conn.close()
    
    if not result:
        bot.reply_to(message, 'Сначала заверши цикл сна командой /wake')
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
            'UPDATE sleep_data SET sleep_mark = ? WHERE user_id = ? AND id = (SELECT max(id) FROM sleep_data WHERE user_id = ? AND sleep_mark IS NULL)',
            (mark, user_id, user_id)
        )
        conn.commit()
        conn.close()

        bot.reply_to(message, f'Оценка сна: {mark} баллов. Хочешь добавить заметку? (/note)')

    except ValueError:
        bot.reply_to(message, 'Пожалуйста, выбери число от 1 до 5.')
        return rate_sleep(message)

@bot.message_handler(commands=['note'])
def add_note(message):
    user_id = message.from_user.id

    conn = sqlite3.connect(SQL_BASE)
    cursor = conn.cursor()
    cursor.execute(
        'SELECT id FROM sleep_data WHERE user_id = ? AND stop_sleep IS NOT NULL AND note IS NULL',
        (user_id,)
    )
    result = cursor.fetchone()
    conn.close()
    
    if not result:
        bot.reply_to(message, 'Сначала заверши цикл сна командой /wake')
        return

    msg = bot.send_message(message.chat.id, 'Напиши заметку о сне:')
    bot.register_next_step_handler(msg, set_note)

def set_note(message):
    user_id = message.from_user.id
    note = message.text

    conn = sqlite3.connect(SQL_BASE)
    cursor = conn.cursor()
    cursor.execute(
        'UPDATE sleep_data SET note = ? WHERE user_id = ? AND id = (SELECT max(id) FROM sleep_data WHERE user_id = ? AND note IS NULL)',
        (note, user_id, user_id)
    )
    conn.commit()
    conn.close()

    bot.reply_to(message, 'Заметка добавлена! Не забудь нажать /sleep перед сном или /stats, чтобы посмотреть последние 5 записей о твоем сне')

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

    stats_message = 'Статистика снов:\n\n'
    stats_message += "".join(
    f'Запись {i+1}:\n'
    f'Начало: {row[0]}\n'
    f'Конец: {row[1]}\n'
    f'Продолжительность: {row[2]}\n'
    f'Оценка: {row[3] or "еще не оценено"}\n'
    f'Заметка: {row[4] or "нет заметки"}\n\n'
    for i, row in enumerate(results)
    )

    bot.reply_to(message, stats_message)

if __name__ == '__main__':
    bot.polling(none_stop=True)