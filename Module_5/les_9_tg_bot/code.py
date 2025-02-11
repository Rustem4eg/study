import telebot
import datetime
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
        return data.get(user_id, {}).get('start_time') if user_id in data else None
    except Exception as e:
        print(e)
    return None

# Основная функция для обработки команды /start
@bot.message_handler(commands=['start'])
def start_command(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    bot.send_message(chat_id, "Привет! Я бот для отслеживания сна. Используй команды /sleep и /wake.")

# Основная функция для обработки команды /sleep
@bot.message_handler(commands=['sleep'])
def sleep_command(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    start_time = datetime.datetime.now()
    save_sleep_data(user_id, start_time, 0, '')
    bot.send_message(chat_id, "Отправляйся спать. Утром сообщи, когда проснешься.")

# Основная функция для обработки команды /wake
@bot.message_handler(commands=['wake'])
def wake_command(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    wake_time = datetime.datetime.now()
    start_time = load_sleep_data(user_id)

    # Корректное вычисление продолжительности сна
    if start_time is not None:
        start_time = datetime.datetime.fromisoformat(start_time)
        duration = wake_time - start_time

        quality = message.text.split(maxsplit=1)[0] if len(message.text.split(maxsplit=1)) > 1 else ''
        notes = message.text.split(maxsplit=1)[1] if len(message.text.split(maxsplit=1)) > 1 else ''
        save_sleep_data(user_id, wake_time, duration.total_seconds(), quality, notes)

        bot.send_message(chat_id, f"Ты спал(а) {duration/3600:.2f} часов. Качество сна: {quality}. Заметки: {notes}.")
    else:
        bot.send_message(chat_id, "Не удалось определить начало сна. Используй /sleep перед /wake.")

# Запуск бота
bot.polling()