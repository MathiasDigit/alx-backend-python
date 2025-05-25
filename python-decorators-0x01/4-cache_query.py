import time
import sqlite3 
import functools

query_cache = {}

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

def cache_query(func):
    """A decorator that implements memoization.""" 
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if args and not kwargs:
            query = args[1]
        elif kwargs:
            query = kwargs['query']
            cached_result = query_cache.get(query)
            if cached_result:
                print('Loaded from cache') 
                return cached_result
            print('Executing')
            result = func(*args, **kwargs)
            query_cache[query] = result
        return result
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")