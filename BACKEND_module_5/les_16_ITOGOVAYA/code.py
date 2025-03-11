import csv
import json
from pathlib import Path

# Определение пути к текущему файлу
current_file = Path(__file__).resolve()
BASE_DIR = current_file.parent

# Задание 0. Работа с json
# Чтение данных из файла student_list.json
jsn_file = BASE_DIR / 'student_list.json'
with open(jsn_file, 'r') as file:
    students = json.load(file)

# Задание 1
def get_average_score(students):
    for student, info in students.items():
        total_score = 0
        num_subjects = 0
        for grade in info['grades'].values():
            total_score += grade
            num_subjects += 1
        average_score = total_score / num_subjects if num_subjects else 0
        print(f"Средний балл для студента {student}: {average_score}")

get_average_score(students)

# Задание 2
def get_average_score(students):
    total_score = 0
    num_subjects = 0
    for grade in students['grades'].values():
        total_score += grade
        num_subjects += 1
    return total_score / num_subjects if num_subjects else 0

def get_best_student(students):
    best_student = None
    highest_average = 0
    for student, info in students.items():
        average_score = get_average_score(info)
        if average_score > highest_average:
            highest_average = average_score
            best_student = student
    return f'Лучший студент {best_student}: средний балл {highest_average}'

def get_worst_student(students):
    worst_student = None
    lowest_average = float('inf')
    for student, info in students.items():
        average_score = get_average_score(info)
        if average_score < lowest_average:
            lowest_average = average_score
            worst_student = student
    return f'Худший студент {worst_student}: средний балл {lowest_average}'

print(get_best_student(students))
print(get_worst_student(students))

# Задание 3
def find_student(name):
    student = students.get(name)
    if student:
        print(f"Имя: {name}")
        print(f"Возраст: {student['age']}")
        print(f"Предметы: {student['subjects']}")
        print(f"Оценки: {student['grades']}")
    else:
        print("Студент с таким именем не найден")

find_student("John")
find_student("Emma")

# Задание 4
def sort_students_by_average_score(students):
    # Вычисляем средние баллы и сохраняем их вместе с именами студентов
    average_scores = {student: get_average_score(info) for student, info in students.items()}
    
    # Сортируем студентов по среднему баллу в порядке убывания
    sorted_students = sorted(average_scores.items(), key=lambda item: item[1], reverse=True)
    
    # Выводим результат
    print("Сортировка студентов по среднему баллу:")
    for student, average_score in sorted_students:
        print(f"{student}: {average_score:.2f}")

sort_students_by_average_score(students)

# Задание 5
# Преобразование словаря в список словарей
students_dict = students
students_list = []
for name, info in students_dict.items():
    student_info = {
        'name': name,
        'age': info['age'],
        'subjects': info['subjects'],
        'grades': info['grades']
    }
    students_list.append(student_info)

# Вывод преобразованного списка
print(students_list)

# Задание 6
# Функция для вычисления среднего балла
def calculate_average_grade(grades):
    total = sum(grades.values())
    return total / len(grades)

# Создание списка данных для CSV
csv_data = []
for name, info in students_dict.items():
    average_grade = calculate_average_grade(info['grades'])
    csv_data.append({'name': name, 'age': info['age'], 'grade': average_grade})

csv_file = BASE_DIR / 'students.csv'
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['name', 'age', 'grade'])
    writer.writeheader()
    for data in csv_data:
        writer.writerow(data)

print("Файл students.csv успешно создан.") 