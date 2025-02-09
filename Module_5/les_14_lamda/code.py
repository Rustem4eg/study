# 1. Дан список строк ["apple", "kiwi", "banana", "fig"]. 
# Оставьте в нем только строки, длина которых больше 4 символов, используя filter() и лямбда-функцию.
fruits = ['apple', 'kiwi', 'banana', 'fig']
fruits_filtered = list(filter(lambda x: len(x) > 4, fruits))
print('1', fruits_filtered)

# 2. Дан список словарей students = [{"name": "John", "grade": 90}, 
# {"name": "Jane", "grade": 85}, {"name": "Dave", "grade": 92}]. 
# Найдите студента с максимальной оценкой, используя max() и лямбда-функцию для задания ключа сортировки.

students = [
            {"name": "John", "grade": 99}, 
            {"name": "Jane", "grade": 85}, 
            {"name": "Dave", "grade": 92}
            ]

max_student = max(students, key = lambda student: student['grade'])
print('2', max_student)

# 3.  Дан список кортежей [(1, 5), (3, 2), (2, 8), (4, 3)]. 
# Отсортируйте его по сумме элементов каждого кортежа с использованием sorted() и лямбда-функции.
tuples = [(1, 5), (3, 2), (2, 8), (4, 3)]
sorted_tuples = sorted(tuples, key = lambda x: x[0] * x[1])
print('3', sorted_tuples)

# 4. Дан список чисел [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. Оставьте в нем только четные числа 
# с использованием filter() и лямбда-функции.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print('4', even_numbers)

# 5. Сортировка объектов пользовательского класса:
# Создайте класс Person с атрибутами name и age. Дан список объектов этого класса. 
# Отсортируйте список объектов по возрасту с использованием sorted() и лямбда-функции.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'имя: {self.name} возраст: {self.age} лет'
    
persons = [
    Person('Рустем', 39),
    Person('Ленара', 10),
    Person('Динар', 13),
    Person('Эльвира', 36)
]

sorted_persons = sorted(persons, key = lambda x: x.age)
print('5', sorted_persons)