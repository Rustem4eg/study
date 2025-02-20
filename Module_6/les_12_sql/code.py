import sqlite3
from pathlib import Path

CURRENT_FILE = Path(__file__).resolve()
BASE_DIR = CURRENT_FILE.parent
SQL_BASE = BASE_DIR / 'library.db'

# Создание базы данных и подключение к ней
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# Создание таблицы books
cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER
)
''')
conn.commit()

# Функция для добавления новой книги
def add_book(title, author, year):
    cursor.execute('''
    INSERT INTO books (title, author, year) VALUES (?, ?, ?)
    ''', (title, author, year))
    conn.commit()

# Функция для получения всех книг
def get_all_books():
    cursor.execute('''
    SELECT * FROM books
    ''')
    return cursor.fetchall()

# Функция для обновления информации о книге
def update_book(book_id, title, author, year):
    cursor.execute('''
    UPDATE books SET title = ?, author = ?, year = ? WHERE id = ?
    ''', (title, author, year, book_id))
    conn.commit()

# Функция для удаления книги по идентификатору
def delete_book(book_id):
    cursor.execute('''
    DELETE FROM books WHERE id = ?
    ''', (book_id,))
    conn.commit()

# Тестовый код
if __name__ == "__main__":
    # Добавление новых книг
    add_book("1984", "George Orwell", 1949)
    add_book("Animal Farm", "George Orwell", 1945)
    add_book("Fahrenheit 451", "Ray Bradbury", 1953)

    # Получение и вывод всех книг
    books = get_all_books()
    print("Все книги:")
    for book in books:
        print(book)

    # Обновление информации о книге
    update_book(1, "Nineteen Eighty-Four", "George Orwell", 1949)
    books = get_all_books()
    print("\nКниги после обновления:")
    for book in books:
        print(book)

    # Удаление книги
    delete_book(2)
    books = get_all_books()
    print("\nКниги после удаления:")
    for book in books:
        print(book)

# Закрытие соединения с базой данных
conn.close()