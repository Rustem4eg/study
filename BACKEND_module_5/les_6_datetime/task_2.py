import datetime

# Запрос даты у пользователя
user_input = input("Введите дату в формате 'год-месяц-день': ")

# Преобразование введенной строки в объект даты
try:
    input_date = datetime.datetime.strptime(user_input, '%Y-%m-%d')
except ValueError:
    print("Некорректный формат даты. Пожалуйста, введите дату в формате 'год-месяц-день'.")
    exit()

# Получение текущей даты
now_date = datetime.datetime.now()

# Вычисление разницы между введенной датой и текущей датой
delta = input_date - now_date

# Вычисление оставшихся дней
remaining_days = delta.days

# Преобразование разницы в дни, часы и минуты
days, seconds = divmod(delta.total_seconds(), 86400)
hours, seconds = divmod(seconds, 3600)
minutes, seconds = divmod(seconds, 60)

# Вывод результата
print(f"До введенной даты осталось {remaining_days} дней.")
print(f"Это {days} дней, {hours} часов и {minutes} минут(ы).")