import os
from mysql.connector import connect
from dotenv import load_dotenv

load_dotenv()

user = os.getenv('user')
password = os.getenv('password')
database = os.getenv('database')

def stream_users():
    """
    Generator function that retrieves rows individually from the user_data table.
    Each iteration yields a single row as a dictionary.
    """
    try:
        connection = connect(
            host='localhost',
            user=user, 
            password=password,
            database=database
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data;")

       # Fetch one row at a time, yield it, and repeat until no rows remain
        row = cursor.fetchone()
        while row is not None:
            yield row
            row = cursor.fetchone()

    except Exception as e:
        print(f"Error while streaming rows: {e}")
    finally:
        cursor.close()
        connection.close()

