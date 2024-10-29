# database.py - Модуль для управления базой данных

import psycopg2
from psycopg2 import sql
from contextlib import closing

# Настройки подключения к базе данных
DB_CONFIG = {
    'dbname': 'your_db_name',
    'user': 'your_user',
    'password': 'your_password',
    'host': 'localhost',
    'port': '5432'
}

def connect_db():
    """Устанавливает подключение к базе данных PostgreSQL."""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        print("Подключение к базе данных установлено.")
        return conn
    except Exception as e:
        print(f"Ошибка подключения к базе данных: {e}")
        return None

def create_tables(conn):
    """Создает необходимые таблицы в базе данных."""
    with closing(conn.cursor()) as cursor:
        create_books_table = """
        CREATE TABLE IF NOT EXISTS books (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            author VARCHAR(255) NOT NULL,
            published_date DATE,
            available BOOLEAN DEFAULT TRUE
        );
        """
        
        create_users_table = """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(255) UNIQUE NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL,
            registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """

        cursor.execute(create_books_table)
        cursor.execute(create_users_table)
        conn.commit()
        print("Таблицы созданы.")

def execute_query(conn, query, params=None):
    """Выполняет SQL-запрос к базе данных."""
    with closing(conn.cursor()) as cursor:
        try:
            cursor.execute(query, params)
            conn.commit()
            print("Запрос выполнен успешно.")
        except Exception as e:
            print(f"Ошибка выполнения запроса: {e}")
            conn.rollback()

def fetch_all(conn, query, params=None):
    """Получает все результаты выполнения запроса."""
    with closing(conn.cursor()) as cursor:
        cursor.execute(query, params)
        return cursor.fetchall()

# Пример использования
if __name__ == "__main__":
    connection = connect_db()
    if connection:
        create_tables(connection)
        
        # Пример добавления книги
        insert_book_query = """
        INSERT INTO books (title, author, published_date) VALUES (%s, %s, %s);
        """
        execute_query(connection, insert_book_query, ('1984', 'George Orwell', '1949-06-08'))

        # Пример получения всех книг
        select_books_query = "SELECT * FROM books;"
        books = fetch_all(connection, select_books_query)
        print(books)

        # Закрытие соединения
        connection.close()