from collections import Counter
from collections import namedtuple
from collections import defaultdict
from collections import deque
import random

# Задание 1
# Генерация случайного списка чисел
random_list = [random.randint(1, 10) for _ in range(20)]
print("Случайный список чисел:", random_list)

# Подсчет уникальных элементов и их количества с помощью Counter
counted = Counter(random_list)
print("Количество уникальных элементов:", len(counted))

# Находим три наиболее часто встречающихся элемента
most_common = counted.most_common(3)
print("Три наиболее часто встречающихся элемента:")
for element, count in most_common:
    print(f"{element} - {count} раз(а)")

# Задание 2
# Создаем именованный кортеж Book с полями title, author, genre
Book = namedtuple('Book', ['title', 'author', 'genre'])

# Создаем несколько экземпляров Book
book1 = Book('Мастер и Маргарита', 'Михаил Булгаков', 'Роман')
book2 = Book('1984', 'Джордж Оруэлл', 'Антиутопия')
book3 = Book('Война и мир', 'Лев Толстой', 'Роман-эпопея')
book4 = Book('Над пропастью во ржи', 'Джером Сэлинджер', 'Роман')

# Выводим информацию о книгах, используя атрибуты именованных кортежей
print("Информация о книгах:")
print(f"Книга 1: {book1.title} - автор: {book1.author} - жанр: {book1.genre}")
print(f"Книга 2: {book2.title} - автор: {book2.author} - жанр: {book2.genre}")
print(f"Книга 3: {book3.title} - автор: {book3.author} - жанр: {book3.genre}")
print(f"Книга 4: {book4.title} - автор: {book4.author} - жанр: {book4.genre}")

# Задание 3
# Создаем defaultdict с типом данных list
book_dict = defaultdict(list)

# Добавляем несколько элементов в словарь
book_dict['Python'].append('Автореферат по Python')
book_dict['Python'].append('Python для начинающих')
book_dict['Python'].append('Продвинутый Python')

book_dict['JavaScript'].append('Изучаем JavaScript')
book_dict['JavaScript'].append('Современный JavaScript')

book_dict['Ruby'].append('Язык программирования Ruby')

# Выводим содержимое словаря, где значения - это списки элементов с одинаковыми ключами
print("Содержимое словаря:")
for key, value in book_dict.items():
 print(f"{key}: {value}")

 # Задание 4
# Создание deque и добавление элементов
deques = deque()

# Добавление элементов в конец deque
deques.append('Элемент 1')
deques.append('Элемент 2')
deques.append('Элемент 3')
deques.append('Элемент 4')

print("Исходный deque: ", deque)

# Добавление элемента в начало deque с помощью appendleft
deques.appendleft('Элемент 0')
print("После appendleft: ", deques)

# Удаление элемента с конца deque с помощью pop
removed_element = deques.pop()
print("После pop: ", deques)
print("Удаленный элемент: ", removed_element)

# Удаление элемента с начала deque с помощью popleft
removed_element = deques.popleft()
print("После popleft: ", deques)
print("Удаленный элемент: ", removed_element)

# Добавление элемента в конец deque снова
deques.append('Элемент 5')
print("После append: ", deques)

# Задание 5
# Функция для добавления элемента в конец очереди
def enqueue(queues, element):
    queues.append(element)

# Функция для извлечения элемента из начала очереди
def dequeue(queues):
    if len(queues) > 0:
        return queues.popleft()
    else:
        return "Очередь пуста"

# Создание пустого deque для очереди
queues = deque()

# Добавление элементов в очередь с помощью функции enqueue
enqueue(queues, "Элемент 1")
enqueue(queues, "Элемент 2")
enqueue(queues, "Элемент 3")
enqueue(queues, "Элемент 4")

# Извлечение элементов из очереди и вывод результата
print("Элементы очереди:")
print(dequeue(queues)) # Извлекаем и выводим первый элемент
print(dequeue(queues)) # Извлекаем и выводим второй элемент
print(dequeue(queues)) # Извлекаем и выводим третий элемент
print(dequeue(queues)) # Извлекаем и выводим четвертый элемент
print("Очередь после операций:")
print(queues) # Оставшиеся элементы в очереди