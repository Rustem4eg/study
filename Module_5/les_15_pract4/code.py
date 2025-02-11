# 1. Дан словарь учеников. Отсортировать учеников по возрасту.
students_dict = {
 'Саша': 27,
 'Кирилл': 52, 
 'Маша': 14, 
 'Петя': 36, 
 'Оля': 43, 
}

sorted_students = sorted(students_dict.items(), key = lambda x: x[1])
print('1. Отсортировано по возрасту: ', sorted_students)

# 2.Дан список с данными о росте и весе людей. Отсортировать их по индексу массы тела. Он вычисляется по формуле: 
# Вес тела в килограммах/(Рост в метрах∗Рост в метрах)

data = [
    (82, 191),
    (68, 174),
    (90, 189), 
    (73, 179), 
    (76, 184)
]

def index_body(x, y):
    return x / (x * y)

sorted_data = list(sorted(data, key = lambda x: x[0] / (x[1]) ** 2))
print('2. Сортировка по индексу массу тела', sorted_data)

# Задача 3
# Дан словарь учеников. Найти самого минимального ученика по возрасту.

students_list = [
    {
        "name": "Саша",
        "age": 27,
    },
    {
        "name": "Кирилл",
        "age": 52,
    },
    {
        "name": "Маша",
        "age": 14,
    },
    {
        "name": "Петя",
        "age": 36,
    },
    {
        "name": "Оля",
        "age": 43,
    },
]

student_min_age = min(students_list, key = lambda student: student['age'])
print(f'3. Самый молодой ученик: {student_min_age['name']} {student_min_age['age']} лет')