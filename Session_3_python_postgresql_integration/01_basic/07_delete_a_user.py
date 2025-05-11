import psycopg2
from psycopg2 import OperationalError

def delete_user_by_id(user_id):
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

        # Check if user exists
        cursor.execute("SELECT name, email FROM users WHERE id = %s;", (user_id,))
        user = cursor.fetchone()

        if user is None:
            print(f"No user found with ID: {user_id}")
            return

        # Ask for confirmation
        print(f"\nConfirm deletion of user: {user[0]} ({user[1]})")
        confirm = input("Type 'yes' to confirm: ").strip().lower()

        if confirm == 'yes':
            cursor.execute("DELETE FROM users WHERE id = %s;", (user_id,))
            connection.commit()
            print(f"User ID {user_id} deleted successfully!")
        else:
            print("Deletion cancelled.")

        cursor.close()
        connection.close()

    except OperationalError as e:
        print("Error during deletion process.")
        print(f"Error: {e}")

if __name__ == "__main__":
    print("🗑Delete User")
    try:
        uid = int(input("Enter user ID to delete: ").strip())
        delete_user_by_id(uid)
    except ValueError:
        print("Invalid input. Please enter a numeric ID.")
