import time
import sqlite3 
import functools

def with_db_connection(func):
     """
    A decorator that injects a database connection 
    into the decorated function automatically.
    """
     @functools.wraps(func)
     def wrapper(*args, **kwargs):
          connection =  sqlite3.connect('users.db')
          try:
               results = func(connection, *args, **kwargs)
               return results
          finally:
               connection.close()
     return wrapper

def retry_on_failure(retries=3, delay=2):
     def decorator(func):
         @functools.wraps(func)
         def wrapper(*args, **kwargs):
              for attempt in range(retries+1):
                   try:
                       result = func(*args, **kwargs)
                       return result
                   except Exception as error:
                        print(f'An error occured retrying operation') 
                        if attempt < retries:
                             print(f"Retrying in {delay} second(s)...")
                             time.sleep(delay)
                        else:
                             print("All attempts failed.")
                             raise
         return wrapper
     return decorator  

                   



@with_db_connection
@retry_on_failure(retries=3, delay=1)

def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

#### attempt to fetch users with automatic retry on failure

users = fetch_users_with_retry()
print(users)