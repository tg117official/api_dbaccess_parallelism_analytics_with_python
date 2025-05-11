import psycopg2
from psycopg2 import OperationalError

def connect_to_postgres():
    try:
        # Modify these credentials based on your setup
        connection = psycopg2.connect(
            dbname="training_db",
            user="postgres",         # change if your user is different
            password="root",  # replace with your actual password
            host="localhost",
            port="5432"              # default port for PostgreSQL
        )

        print("Connection to training_db successful!")

        # It's good practice to close the connection if not in use
        connection.close()

    except OperationalError as e:
        print("Connection failed!")
        print(f"Error details: {e}")

if __name__ == "__main__":
    connect_to_postgres()
