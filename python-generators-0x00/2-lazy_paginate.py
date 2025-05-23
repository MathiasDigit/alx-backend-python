import os
from mysql.connector import connect 
from dotenv import load_dotenv

load_dotenv()

user = os.getenv('user')
password = os.getenv('password')
database = os.getenv('database')

def paginate_users(page_size, offset):
    """
    Retrieves a fixed number of users from the database starting at a specific offset.
    Arguments:
        page_size: Number of rows to return
        offset: How many rows to skip before starting the selection
    """
    try:
        db = connect(
            host = 'localhost',
            user=user,
            password=password,
            database=database
         )
        cursor = db.cursor(dictionary=True)
        cursor.execute(
            """SELECT * FROM user_data LIMIT %s OFFSET %s""",
            (page_size, offset)
        )
        return cursor.fetchall()
    except Exception as e:
        print(f"An error occurred while fetching users: {e}")
        return []
    finally:
        cursor.close()
        db.close()
        
def lazy_paginate(page_size):
    """
    Generator function that lazily yields pages of users from the database.
    Arguments:
        page_size: Number of users per page
    """

    offset = 0
    while True:
        users = paginate_users(page_size, offset)
        if not users:
            break
        yield users
        offset += page_size 