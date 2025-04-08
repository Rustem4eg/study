import sqlite3
from pathlib import Path

CURRENT_FILE = Path(__file__).resolve()
BASE_DIR = CURRENT_FILE.parent
SQL_BASE = BASE_DIR / 'library.db'

conn = sqlite3.connect(SQL_BASE)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER
)
''')
conn.commit()

def add_book(title, author, year):
    cursor.execute('''
    INSERT INTO books (title, author, year) VALUES (?, ?, ?)
    ''', (title, author, year))
    conn.commit()

def get_all_books():
    cursor.execute('''
    SELECT * FROM books
    ''')
    return cursor.fetchall()

def update_book(book_id, title, author, year):
    cursor.execute('''
    UPDATE books SET title = ?, author = ?, year = ? WHERE id = ?
    ''', (title, author, year, book_id))
    conn.commit()

def delete_book(book_id):
    cursor.execute('''
    DELETE FROM books WHERE id = ?
    ''', (book_id,))
    conn.commit()

if __name__ == "__main__":
    add_book("Война и мир", "Лев Толстой", 1869)
    add_book("Преступление и наказание", "Федор Достоевский", 1866)
    add_book("Мертвые души", "Николай Гоголь", 1842)

    books = get_all_books()
    print("Все книги:")
    for book in books:
        print(book)

    update_book(1, "Маша и Медведь", "Медведь Петрович", 2024)
    books = get_all_books()
    print("\nКниги после обновления:")
    for book in books:
        print(book)

    delete_book(2)
    books = get_all_books()
    print("\nКниги после удаления:")
    for book in books:
        print(book)

conn.close()