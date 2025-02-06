import telebot
import datetime
import time
import json

# Переменные окружения
TOKEN = '8063391832:AAGlsqsWs1ODOE2fznIERykoxVfPmi3JwFM'

# Инициализация бота
bot = telebot.TeleBot(TOKEN)

# Функция для сохранения данных сна
def save_sleep_data(user_id, start_time, duration, quality, notes=''):
    data = {user_id: {'start_time': str(start_time), 'duration': duration, 'quality': quality, 'notes': notes}}
    with open('sleep_data.json', 'w') as outfile:
        json.dump(data, outfile)

# Функция для загрузки данных сна
def load_sleep_data(user_id):
    data = {}
    try:
        with open('sleep_data.json', 'r') as infile:
            data = json.load(infile)
        return data.get(user_id, {}).get('start_time') if user_id in data else {}
    except Exception as e:
        print(e)
    return {}

# Основная функция для обработки команд
@bot.message_handler(commands=['start', 'sleep', 'wake'])
def handle_message(message):
    user_id = message.from_user.id
    chat_id = message.chat.id

    # Проверка на команду /start
    if message.text.lower() == "/start":
        bot.send_message(chat_id, "Привет! Я бот для отслеживания сна. Используй команды /sleep и /wake.")

    # Проверка на команду /sleep
    elif message.text.lower() == "/sleep":
        start_time = datetime.datetime.now()
        save_sleep_data(user_id, start_time, 0, '')
        bot.send_message(chat_id, "Отправляйся спать. Утром сообщи, когда проснешься.")

    # Проверка на команду /wake
    elif message.text.lower() == "/wake":
        wake_time = datetime.datetime.now()
        start_time = load_sleep_data(user_id)

        # Корректное вычисление продолжительности сна
        if isinstance(start_time, dict) and 'start_time' in start_time:
            duration = wake_time - datetime.datetime.fromisoformat(start_time['start_time'])
        else:
            duration = wake_time - start_time

        quality = message.text.split(maxsplit=1)[0] if len(message.text.split(maxsplit=1)) > 1 else ''
        notes = message.text.split(maxsplit=1)[1] if len(message.text.split(maxsplit=1)) > 1 else ''
        save_sleep_data(user_id, start_time, duration.total_seconds(), quality, notes)

        bot.send_message(chat_id, f"Ты спал(а) {duration/3600:.2f} часов. Качество сна: {quality}. Заметки: {notes}.")
    else:
        bot.send_message(chat_id, "Неизвестная команда. Используй /start, /sleep или /wake.")

# Запуск бота
bot.polling()