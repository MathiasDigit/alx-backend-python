"""A script that manages SQLite database connections using a Python decorator."""
import sqlite3
import functools

def with_db_connection(func):
    """
    A decorator that injects a database connection 
    into the decorated function automatically.
    """
    @functools.wraps(func)
    def wrapper(*args, **Kwargs):
        connection = sqlite3.connect('users.db')
        try:
            results = func(connection, *args, **Kwargs)
            return results
        finally:
            connection.close()
    return wrapper
    

@with_db_connection
def get_user_by_id(conn, user_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()

#### Fetch user by ID with automatic connection handling 
user = get_user_by_id(user_id=1)
print(user)