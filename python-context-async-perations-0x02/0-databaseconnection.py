"""This script implements a class-based context manager that executes a SQL query."""

import sqlite3

class ExecuteQuery:
    def __init__(self, query, param):
        self.query = query
        self.param = (param,)

    def __enter__(self):
        self.conn = sqlite3.connect('users.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.query, self.param)
        return self.cursor.fetchall()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.conn.close()

with ExecuteQuery("SELECT * FROM users WHERE age > ?", 25) as result:
    print(result)