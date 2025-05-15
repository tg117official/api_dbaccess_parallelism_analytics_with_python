import psycopg2
from psycopg2 import OperationalError, IntegrityError

def update_user_email(user_id, new_email):
    try:
        # Connect to PostgreSQL
        connection = psycopg2.connect(
            dbname="training_db",
            user="postgres",
            password="root",  # Replace securely
            host="localhost",
            port="5432"
        )
        cursor = connection.cursor()

        # First, check if user exists
        cursor.execute("SELECT id FROM users WHERE id = %s;", (user_id,))
        if cursor.fetchone() is None:
            print(f"No user found with ID: {user_id}")
            return

        # Proceed with update
        update_query = "UPDATE users SET email = %s WHERE id = %s;"
        cursor.execute(update_query, (new_email, user_id))
        connection.commit()

        print(f"Email updated successfully for user ID {user_id}!")

        # Clean up
        cursor.close()
        connection.close()

    except IntegrityError:
        print("Email must be unique. Another user has this email.")
    except OperationalError as e:
        print("Connection or execution failed.")
        print(f"Error: {e}")

if __name__ == "__main__":
    print("Update User Email")
    try:
        uid = int(input("Enter user ID to update: ").strip())
        email = input("Enter new email: ").strip()
        update_user_email(uid, email)
    except ValueError:
        print("Invalid input. Please enter a valid numeric ID.")
