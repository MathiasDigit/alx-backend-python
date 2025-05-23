import os
from mysql.connector import connect
from dotenv import load_dotenv

load_dotenv()

user = os.getenv('user')
password = os.getenv('password')
database = os.getenv('database')

def stream_users_in_batches(batch_size):
    """
    Generator that retrieves multiple records per batch from the user_data table.
    """
    try:
        db = connect(
            host= 'localhost',
            user=user,
            password=password,
            database=database
        )
        cursor = db.cursor(dictionary=True)
        cursor.execute(
            """
            SELECT * FROM user_data LIMIT %s
            """,
            (batch_size,)
        )

        # Infinite loop to fetch next set of records until empty
        while True:
            batch = cursor.fetchmany(batch_size)
            if not batch:
                break
            yield batch
    except Exception as e:
        print(f"Failed to retrieve batches: {e}")
    finally:
        cursor.close()
        db.close()


def batch_processing(batch_size):
    """
    Function that applies a filtering rule on each batch: keep users above age 25.
    """
    for batch in stream_users_in_batches(batch_size):
        # Inline loop for processing each row inside the batch
        filtered = [user for user in batch if user['age'] > 25]
        for user in filtered:
            print(user)
        return filtered
