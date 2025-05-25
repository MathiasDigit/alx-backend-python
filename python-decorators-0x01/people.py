""" A script that peoples my sqlite3 database."""

import csv
import sqlite3

def database(): 
    connection = sqlite3.connect('users.db')

    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER
        );
        """
    )
    connection.commit()
    return cursor, connection

with open('./data.csv', encoding='utf-8') as file:
    file_iterator = csv.reader(file)
    database_tools = database()
    cursor, connection = database_tools
    next(file_iterator)
    for row in file_iterator:
        name = row[0]
        email = row[1]
        age = row[2]
        cursor.execute(
            """
            INSERT INTO users(name, email, age) VALUES(?, ?, ?)
            """,
            (name, email, age)
        )
    connection.commit()
    cursor.close()
    connection.close() 