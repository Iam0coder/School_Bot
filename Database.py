import sqlite3


def init_db():
    # Подключение к базе данных (создастся, если её нет)
    conn = sqlite3.connect('school_data.db')
    cur = conn.cursor()
    # Создание таблицы students
    cur.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        grade TEXT NOT NULL)
    ''')
    conn.commit()
    conn.close()


# Инициализация базы данных
init_db()
