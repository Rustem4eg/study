import datetime

# Получите текущую дату и время.
now = datetime.datetime.now()
print('Текущая дата и время: ', now)

# Выведите на экран день недели для этой даты.
current_date = datetime.date.fromtimestamp(now.timestamp())
days_of_week = [
    "понедельник",
    "вторник",
    "среда",
    "четверг",
    "пятница",
    "суббота",
    "воскресенье"
]
weekday_number = current_date.weekday()
print("Сегодня:", days_of_week[weekday_number])

# Определите, является ли год текущей даты високосным, и выведите соответствующее сообщение.
current_year = current_date.year

if (current_year % 4 == 0) and (current_year % 100 != 0) or (current_year % 400 == 0):
    print(f"Текущий год {current_year} является високосным.")
else:
    print(f"Текущий год {current_year} не является високосным.")

