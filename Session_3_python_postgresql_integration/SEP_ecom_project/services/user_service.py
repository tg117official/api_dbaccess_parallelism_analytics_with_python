# services/user_service.py

from services.db import get_connection

def get_user_by_username(username):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT username, email, password, role
                FROM users
                WHERE username = %s
            """, (username,))
            row = cur.fetchone()
            if row:
                return {
                    "username": row[0],
                    "email": row[1],
                    "password": row[2],
                    "role": row[3]
                }
    return None


def validate_user(username, password):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT username, email, role
                FROM users
                WHERE username = %s AND password = %s
            """, (username, password))
            row = cur.fetchone()
            if row:
                return {
                    "username": row[0],
                    "email": row[1],
                    "role": row[2]
                }
    return None


def email_exists(email):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT 1 FROM users WHERE email = %s
            """, (email,))
            return cur.fetchone() is not None


def register_user(user_data):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1 FROM users WHERE username = %s", (user_data['username'],))
                if cur.fetchone():
                    return False, "Username already exists"

                if email_exists(user_data['email']):
                    return False, "Email already exists"

                cur.execute("""
                    INSERT INTO users (username, email, password, role)
                    VALUES (%s, %s, %s, %s)
                """, (user_data['username'], user_data['email'], user_data['password'], user_data['role']))
                conn.commit()
                return True, None
    except Exception as e:
        return False, str(e)


def delete_user(username):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                DELETE FROM users WHERE username = %s
            """, (username,))
            conn.commit()


def update_user_role(username, new_role):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                UPDATE users SET role = %s WHERE username = %s
            """, (new_role, username))
            conn.commit()


def get_all_users():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT username, email, role
                FROM users
                ORDER BY username
            """)
            rows = cur.fetchall()
            return [
                {
                    "username": row[0],
                    "email": row[1],
                    "role": row[2]
                } for row in rows
            ]
