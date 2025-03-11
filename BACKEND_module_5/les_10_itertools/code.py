import itertools
# Задача 1: Комбинации чисел из списка
from itertools import combinations

numbers = [1, 2, 3, 4]
combinations = list(combinations(numbers, 2))

for combination in combinations:
    print(combination)

print('-------------------------------------')
# Задача 2: Перебор перестановок букв в слове

word = 'Python'
letters = list(word)
permutations = list(itertools.permutations(letters))
for p in permutations:
    print("".join(p))
print('-------------------------------------')
# Задача 3: Объединение списков в цикле
from itertools import cycle, islice

list1 = ['a', 'b']
list2 = [1, 2, 3]
list3 = ['x', 'y']
cycled_lists = cycle((list1, list2, list3))
combined_list = []
for _ in range(5):
    for element in islice(cycled_lists, 3):
        combined_list.extend(element)
print(combined_list)
print('-------------------------------------')
# Задача 4: Генерация бесконечной последовательности чисел Фибоначчи
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fibonacci_numbers = fibonacci_generator()

for i in range(10):
    print(next(fibonacci_numbers), end=' ')
print()
print('-------------------------------------')
# Задача 5: Составление всех возможных комбинаций слов
from itertools import product

color_list = ['red', 'blue']
clothing_list = ['shirt', 'shoes']

for combination in product(color_list, clothing_list):
    print(combination)
print('-------------------------------------')