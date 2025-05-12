import psycopg2
from psycopg2 import sql, OperationalError

def create_users_table():
    try:
        # Replace with your actual DB credentials or use environment variables
        connection = psycopg2.connect(
            dbname="training_db",
            user="postgres",
            password="your_password",  # Replace or read from env
            host="localhost",
            port="5432"
        )

        cursor = connection.cursor()

        # Create table SQL
        create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        );
        """

        cursor.execute(create_table_query)
        connection.commit()

        print("✅ 'users' table created successfully.")

        # Clean up
        cursor.close()
        connection.close()

    except OperationalError as e:
        print("❌ Failed to connect or execute query.")
        print(f"Error: {e}")

if __name__ == "__main__":
    create_users_table()
