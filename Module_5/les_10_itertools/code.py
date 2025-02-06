# Задача 1: Комбинации чисел из списка
from itertools import combinations

numbers = [1, 2, 3, 4]
combinations = list(combinations(numbers, 2))

for combination in combinations:
    print(combination)

# Задача 2: Перебор перестановок букв в слове
from itertools import permutations

word = 'Python'
permutations = list(permutations(word))

for permutation in permutations:
    print(permutation)

# Задача 3: Объединение списков в цикле
from itertools import cycle

lists = [['a', 'b'], [1, 2, 3], ['x', 'y']]

for _ in range(5):
    combined_list = [item for item in cycle(*lists).next() for _ in range(len(lists))]
    print(combined_list)

# Задача 4: Генерация бесконечной последовательности чисел Фибоначчи
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fibonacci_numbers = fibonacci()

for i in range(10):
    print(next(fibonacci_numbers))

# Задача 5: Составление всех возможных комбинаций слов
from itertools import product

words_1 = ['red', 'blue']
words_2 = ['shirt', 'shoes']

for combination in product(words_1, words_2):
    print(combination)