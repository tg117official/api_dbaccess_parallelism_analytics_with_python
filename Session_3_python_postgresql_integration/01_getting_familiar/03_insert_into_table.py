import psycopg2
from psycopg2 import OperationalError, IntegrityError

def insert_user(name, email):
    try:
        # Database connection
        connection = psycopg2.connect(
            dbname="training_db",
            user="postgres",
            password="root",  # Replace or use env variable
            host="localhost",
            port="5432"
        )
        cursor = connection.cursor()

        insert_query = """
        INSERT INTO users (name, email)
        VALUES (%s, %s);
        """

        cursor.execute(insert_query, (name, email))
        connection.commit()

        print(f"✅ User '{name}' inserted successfully!")

        cursor.close()
        connection.close()

    except IntegrityError as e:
        print("❌ Email must be unique. Insert failed.")
    except OperationalError as e:
        print("❌ Connection failed.")
        print(f"Error: {e}")

if __name__ == "__main__":
    print("Add New User")
    user_name = input("Enter user name: ").strip()
    user_email = input("Enter user email: ").strip()

    insert_user(user_name, user_email)
