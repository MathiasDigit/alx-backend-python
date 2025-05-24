"""A script that computes the average age of users using a Python generator."""
from dotenv import load_dotenv
import os
from mysql.connector import connect

# Load environment variables from .env file
load_dotenv()
user = os.getenv('user')
password = os.getenv('password')
database = os.getenv('database')

def stream_user_ages():
    """Yield user ages from the database one at a time."""
    try:
        db = connect(
            host='localhost',
            user=user,
            password=password,
            database=database,
        )
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT age FROM user_data;")
        for row in cursor:
            # Deliver each age as it is retrieved from the database
            yield row['age']
    except Exception as error:
        print(f"Failed to stream ages: {error}")
    finally:
        cursor.close()
        db.close()

def average_age():
    """Calculate and display the average age using the age stream."""
    total = 0
    count = 0
    for age in stream_user_ages():
        total += age
        count += 1
    if count > 0:
        print(f"Average age of users: {total / count}")
    else:
        print("No age data found.")
