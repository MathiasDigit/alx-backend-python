# Decorator that logs the SQL query before executing the function
import sqlite3
import functools
from datetime import datetime

#### decorator to lof SQL queries

""" YOUR CODE GOES HERE"""
def log_queries(func):
    """Decorator that logs the SQL query before the function runs."""
    @functools.wraps(func)
    def wrapper(query):
        print(query)
        return func(query)
    return wrapper 

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
# print(users)

