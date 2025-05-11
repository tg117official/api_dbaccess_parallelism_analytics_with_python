# services/user_service.py

from services.file_utils import load_json, write_json

USER_FILE = 'data/users.json'

def get_user_by_username(username):
    users = load_json(USER_FILE)
    return next((u for u in users if u['username'] == username), None)


def validate_user(username, password):
    users = load_json(USER_FILE)
    return next(
        (u for u in users if u['username'] == username and u['password'] == password),
        None
    )


def email_exists(email):
    users = load_json(USER_FILE)
    return any(u.get('email') == email for u in users)


def register_user(user_data):
    users = load_json(USER_FILE)

    if any(u['username'] == user_data['username'] for u in users):
        return False, "Username already exists"

    if email_exists(user_data.get('email')):
        return False, "Email already exists"

    users.append(user_data)
    write_json(USER_FILE, users)
    return True, None


