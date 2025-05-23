import csv
import os
from mysql.connector import connect, Error 
from dotenv import load_dotenv

#Load the environment variables from a .env file
load_dotenv()

#Retrieval of environment variables
user = os.getenv('user')
password = os.getenv('password')
database = os.getenv('database')



def connect_db():
    """ A Function that establishes connection to a Mysql server (without selecting a specific database yet). """
    try:
        connection = connect(
            host='localhost',
            user=user,
            password=password,

        )
        print("✅ Connection to MySQL server established.")
        return connection
    except Error as e: 
        print("❌ Error connecting to MySQL server:", e)
        return None
    

def create_database(connection):
    """
    Creates the database ALX_prodev if it does not exist.
    Arg:
        connection: A connection object to the MySQL server (no database selected yet).
    """
    try:
        with connection.cursor() as cursor:
            cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
            print("✅ Database 'ALX_prodev' created or already exists.")
        connection.commit() 
    except Error as e:
        print("❌ Error creating database:", e)       
    

def connect_to_prodev():
     """A function that establishes a connection and connects to a database."""
     db = connect(
         host='localhost',
         user=user,
         password=password,
         database=database,
     )
     return db 


def create_table(connection):
    """ Creates the 'user_data' table in the database if it does not already exist.
        Args: connection: A MySQL database connection object."""

    with connection.cursor() as cursor:
        cursor.execute(
              """
            CREATE TABLE IF NOT EXISTS user_data (
            user_id CHAR(36) PRIMARY KEY DEFAULT(UUID()),
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL(10, 0) NOT NULL
            )
            """ 
        )
        connection.commit()


def insert_data(connection, data): 
    """
      Inserts data into the 'user_data' table of the ALX_prodev database.

      Args:
      connection: A MySQL database connection object.
      data: Path to a CSV file containing the data to insert.

     Returns:
     None
    """

    with open(data, newline='', encoding='utf-8') as file:
        file_iterator = csv.reader(file)
        next(file_iterator)
        with connection.cursor() as cursor:
            for row in file_iterator:
                name = row[0]
                email = row[1]
                age = row[2]
                cursor.execute(
                    """ 
                    INSERT INTO user_data (name, email, age)
                    VALUES(%s, %s, %s)
                    """,
                    (name, email, age)
                )
            connection.commit()

        