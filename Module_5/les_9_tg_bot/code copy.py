from datetime import datetime, timedelta
import telebot
import os
import json

# Переменные окружения
TOKEN_SLEEP_BOT = '8063391832:AAGlsqsWs1ODOE2fznIERykoxVfPmi3JwFM'

TG_TOKEN = os.getenv('TOKEN_SLEEP_BOT')
bot = telebot.TeleBot('8063391832:AAGlsqsWs1ODOE2fznIERykoxVfPmi3JwFM')
SLEEP_COMMAND = 'sleep'
WAKE_COMMAND = 'wake'

# Функция для записи данных в JSON файл
def write_to_json():
    with open('sleep_data.json', 'w') as outfile:
        json.dump(sleep_dict, outfile, ensure_ascii=False, indent=4)

# Функция для чтения данных из JSON файла
def read_from_json():
    try:
        with open('sleep_data.json', 'r') as infile:
            sleep_dict = json.load(infile)
    except FileNotFoundError:
        print("Файл sleep_data.json не найден. Создаем пустой файл.")
        with open('sleep_data.json', 'w') as outfile:
            json.dump({}, outfile, ensure_ascii=False, indent=4)

# Инициализация глобального словаря
sleep_dict = {}

read_from_json()  # Инициализация данными из JSON, если он существует

@bot.message_handler(commands='start')
def start(message):
    user_id = message.from_user.id
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}.\n'
                      f'Я буду помогать тебе отслеживать параметры сна.\n'
                      f'Введи /{SLEEP_COMMAND} перед сном\n'
                      f'Введи /{WAKE_COMMAND} после пробуждения')


@bot.message_handler(commands=SLEEP_COMMAND)
def sleep(message):
    user_id = message.from_user.id
    start_sl = datetime.now()
    sleep_dict[user_id]['start_sleep'] = start_sl
    bot.send_message(message.chat.id, f'Время начала сна зафиксировано. '
                     f'Не забудь нажать /{WAKE_COMMAND}, когда проснешься')


@bot.message_handler(commands=WAKE_COMMAND)
def wake(message):
    user_id = message.from_user.id
    stop_sl = datetime.now()
    try:
        sleep_dict[user_id]['stop_sleep'] = stop_sl
        long_sl = stop_sl - sleep_dict[user_id]['start_sleep']
        sleep_dict[user_id]['duration'] = convert_timedelta(long_sl)
        bot.send_message(message.chat.id, f'Время пробуждения зафиксировано.\n'
                         f'Ты спал {sleep_dict[user_id]["duration"]}.\n'
                         f'Не забудь отметить начало следующего сна!')
        sleep_dict[user_id] = {}
        write_to_json()  # Запись обновленных данных в JSON
    except KeyError:
        bot.send_message(message.chat.id, 'Ты забыл отметить время начала сна')

def convert_timedelta(dt):
    days, seconds = dt.days, dt.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 60)
    return f'{hours} h, {minutes} min, {seconds} sec'


bot.polling(none_stop=True)