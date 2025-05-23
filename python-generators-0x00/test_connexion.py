from mysql.connector import connect
from dotenv import load_dotenv
import os

load_dotenv()

user = os.getenv('user')
password = os.getenv('password')

try:
    connection = connect(
        host='localhost',
        user=user,
        password=password
    )
    print("Connexion réussie")
    connection.close()
except Exception as e:
    print("Échec :", e)
