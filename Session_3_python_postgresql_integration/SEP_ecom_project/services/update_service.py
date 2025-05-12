import psycopg2
from services.db import get_connection

def update_user(username, updated_data):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Optional: fetch existing user to verify
        cursor.execute("SELECT username FROM users WHERE username = %s", (username,))
        result = cursor.fetchone()

        if not result:
            print("User not found")
            return False

        # Build the update query dynamically
        updates = []
        values = []

        if 'email' in updated_data:
            updates.append("email = %s")
            values.append(updated_data['email'])

        if 'password' in updated_data:
            updates.append("password = %s")
            values.append(updated_data['password'])

        if not updates:
            print("No fields to update")
            return False

        update_query = f"UPDATE users SET {', '.join(updates)} WHERE username = %s"
        values.append(username)

        cursor.execute(update_query, tuple(values))
        conn.commit()
        print("User updated successfully")
        return True

    except Exception as e:
        print("Error:", e)
        return False
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
