from itertools import cycle, islice

list1 = ['a', 'b']
list2 = [1, 2, 3]
list3 = ['x', 'y']

# Создаём бесконечный цикл из трёх списков с помощью itertools.cycle
cycled_lists = cycle((list1, list2, list3))

# Объединяем элементы из трёх списков в один
combined_list = []
for _ in range(5):
    for element in islice(cycled_lists, 3):
        combined_list.extend(element)

# Выводим результат
print(combined_list)