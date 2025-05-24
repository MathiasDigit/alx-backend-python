"""A script that computes the average age of users using a Python generator."""
import os
from mysql.connector import connect
from dotenv import load_dotenv

load_dotenv()

user = os.getenv('user')
password = os.getenv('password')
database = os.getenv('database')

def stream_users_ages():
    """A function"""
    try:
        db = connect(
            host = 'localhost',
            user=user,
            password=password,
            database=database
        )
        cursor = db.cursor(dictionary=True)
        cursor.execute(
            """ SELECT age FROM user_data;"""
        )
        result = cursor.fetchall()
        for age in result:
            yield age
    except Exception as error:
        print(f"An error occured while trying to retrieve age from database: {error}")
    finally:
        cursor.close()
        db.close()

def average_age():
     """Calculate and display the average age using the age stream."""
     age = 0
     count = 0
     for row in stream_users_ages():
         age += row['age']
         count += 1
     if count > 0:
         print(f"Average age of users: {age / count}")
     else:
          print("No age data found.")
