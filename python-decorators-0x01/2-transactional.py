"""
Create a decorator that automatically handles database transactions, 
committing changes on success or rolling back in case of an error.
"""
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

def transactional(func):
    """Decorator that ensures the function runs within a database transaction block."""
    @functools.wraps(func)
    def wrapper(connection, *args, **kwargs):
        """Wrapper function that adds transaction control around the original function."""
        try:
            connection.execute('BEGIN')
            func(connection, *args, **kwargs)
            connection.commit()
        except Exception as error:
            connection.rollback()
    return wrapper


@with_db_connection
@transactional
def Update_user_email(conn, user_id, new_email):
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email = ? WHERE id = ?",(new_email, user_id))

#### Update user's email with automatic transaction handling 
Update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')
