import json
from pathlib import Path

current_file = Path(__file__).resolve()
BASE_DIR = current_file.parent
json_file = BASE_DIR / 'task1.json'


with open(json_file, 'r') as file:
    data = json.load(file)


# Определение общего количества студентов
total_students = len(data)
print(f"Общее количество студентов: {total_students}")

# Поиск студента с самым высоким возрастом
highest_age = 0
highest_age_student = None
for student in data:
    if student["возраст"] > highest_age:
        highest_age = student["возраст"]
        highest_age_student = student

if highest_age_student:
    print(f"Студент с самым высоким возрастом: {highest_age_student['имя']}, {highest_age_student['возраст']}, {highest_age_student['город']}")
else:
    print("Студентов с возрастом больше нет.")

# Определение количества студентов, изучающих Python
python_count = len(list(filter(lambda x: 'Python' in x['предметы'], data)))
print(f"Количество студентов, изучающих Python: {python_count}")


