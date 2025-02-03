import csv
import json
from pathlib import Path

# Функция для чтения данных из JSON файла
def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as json_file:
        employees = json.load(json_file)
    return employees

# Функция для чтения данных из CSV файла
def read_csv_file(file_path):
    result = {}
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            employee_id = row['employee_id']
            performance = float(row['performance'])
            result[employee_id] = performance
    return result

# Функция для вычисления средней производительности
def calculate_average_performance(performance_data):
    total_sum = 0
    count = 0
    for performance in performance_data.values():
        if performance is not None:
            total_sum += performance
            count += 1
    return total_sum / count if count else 0

# Функция для поиска сотрудника с наивысшей производительностью
def find_highest_performance(performance_data):
    highest_performance = 0
    highest_employee = None
    for employee, performance in performance_data.items():
        if performance > highest_performance:
            highest_performance = performance
            highest_employee = employee
    return highest_employee, highest_performance

# Чтение данных из JSON и CSV файлов
BASE_DIR = Path(__file__).resolve().parent
json_file = BASE_DIR / 'employees.json'
csv_file = BASE_DIR / 'performance.csv'

employees_data = read_json_file(json_file)
performance_data = read_csv_file(csv_file)

# Сопоставление данных о производительности с данными о сотрудниках
employee_performances = {}
for employee in employees_data:
    employee_id = employee['id']
    performance = performance_data.get(employee_id, None)
    employee_performances[employee_id] = performance

# Определение средней производительности
average_performance = calculate_average_performance(employee_performances)

# Поиск сотрудника с наивысшей производительностью
highest_employee, highest_performance = find_highest_performance(employee_performances)

# Вывод результатов
print(f"Средняя производительность среди всех сотрудников: {average_performance}")
print(f"Сотрудник с наивысшей производительностью: {highest_employee['имя']} с показателем {highest_performance}")