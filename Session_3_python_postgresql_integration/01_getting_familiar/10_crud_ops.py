import psycopg2
from psycopg2 import OperationalError, IntegrityError

# Database config (replace with secure method in practice)
DB_CONFIG = {
    "dbname": "training_db",
    "user": "postgres",
    "password": "your_password",  # Replace securely
    "host": "localhost",
    "port": "5432"
}

def connect():
    """Establish a PostgreSQL connection."""
    return psycopg2.connect(**DB_CONFIG)

# CREATE
def create_user(name, email):
    try:
        conn = connect()
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO users (name, email) VALUES (%s, %s);",
            (name, email)
        )
        conn.commit()  # Must commit to persist INSERT
        print(f"User '{name}' added successfully.")

        cur.close()
        conn.close()
    except IntegrityError:
        print("Email already exists.")
    except OperationalError as e:
        print("Database connection failed.", e)

# 🔹 READ
def read_users():
    try:
        conn = connect()
        cur = conn.cursor()

        cur.execute("SELECT id, name, email FROM users;")
        users = cur.fetchall()

        print("\nAll Users:")
        for u in users:
            print(f"ID: {u[0]} | Name: {u[1]} | Email: {u[2]}")

        cur.close()
        conn.close()
    except OperationalError as e:
        print("Could not read users.", e)

# UPDATE
def update_email(user_id, new_email):
    try:
        conn = connect()
        cur = conn.cursor()

        cur.execute("UPDATE users SET email = %s WHERE id = %s;", (new_email, user_id))
        if cur.rowcount == 0:
            print(f"No user found with ID {user_id}.")
        else:
            conn.commit()  # Required to apply UPDATE
            print(f"User ID {user_id}'s email updated.")

        cur.close()
        conn.close()
    except IntegrityError:
        print("Email must be unique.")
    except OperationalError as e:
        print("Could not update email.", e)

# DELETE
def delete_user(user_id):
    try:
        conn = connect()
        cur = conn.cursor()

        cur.execute("DELETE FROM users WHERE id = %s;", (user_id,))
        if cur.rowcount == 0:
            print(f"No user found with ID {user_id}.")
        else:
            conn.commit()  # Required to apply DELETE
            print(f"User ID {user_id} deleted.")

        cur.close()
        conn.close()
    except OperationalError as e:
        print("Could not delete user.", e)

# Interactive Menu
def menu():
    while True:
        print("\n==== USER MANAGEMENT MENU ====")
        print("1. Add New User")
        print("2. View All Users")
        print("3. Update User Email")
        print("4. Delete User")
        print("5. Exit")

        choice = input("Enter choice (1-5): ").strip()

        if choice == '1':
            name = input("Name: ")
            email = input("Email: ")
            create_user(name, email)
        elif choice == '2':
            read_users()
        elif choice == '3':
            try:
                uid = int(input("User ID: "))
                new_email = input("New Email: ")
                update_email(uid, new_email)
            except ValueError:
                print("Invalid ID.")
        elif choice == '4':
            try:
                uid = int(input("User ID to delete: "))
                delete_user(uid)
            except ValueError:
                print("Invalid ID.")
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()
