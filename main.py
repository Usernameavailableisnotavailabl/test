# import sqlite3
# import psycopg2

# def create_table():
#     conn = sqlite3.connect('example.db')
#     c = conn.cursor()
#     c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT NOT NULL, age INTEGER)''')
#     conn.commit()
#     conn.close()


import sqlite3
import psycopg2
conn = None
try:
    print('Подключение к базе данных PostgreSQL')
    conn = psycopg2.connect(
        host='localhost',
        dbname='postgres',
        user='postgres',
        password='321654',
        port=5432
    )
    cur = conn.cursor()
    print('Подключено к базе данных PostgreSQL')
    cur.execute('выбор версии()')
    print(cur.fetchone())
    cur.close()
except(Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
        print('Соединение с базой данных закрыто.')



