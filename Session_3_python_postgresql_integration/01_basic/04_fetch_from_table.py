import psycopg2
from psycopg2 import OperationalError

def get_all_users():
    try:
        # Connect to PostgreSQL
        connection = psycopg2.connect(
            dbname="training_db",
            user="postgres",
            password="your_password",  # Replace securely
            host="localhost",
            port="5432"
        )
        cursor = connection.cursor()

        # Fetch users
        cursor.execute("SELECT id, name, email FROM users;")
        users = cursor.fetchall()

        if not users:
            print("No users found in the database.")
        else:
            print("\nList of Users:\n")
            print("{:<5} {:<20} {:<30}".format("ID", "Name", "Email"))
            print("-" * 60)
            for user in users:
                print("{:<5} {:<20} {:<30}".format(user[0], user[1], user[2]))

        # Close connection
        cursor.close()
        connection.close()

    except OperationalError as e:
        print("Failed to fetch users.")
        print(f"Error: {e}")

if __name__ == "__main__":
    get_all_users()
