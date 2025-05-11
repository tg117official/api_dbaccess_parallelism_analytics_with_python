# services/user_service.py
from file_utils import load_json

USER_FILE = 'data/users.json'

def get_user_by_username(username):
    users = load_json(USER_FILE)
    return next((u for u in users if u['username'] == username), None)

def validate_user(username, password):
    user = get_user_by_username(username)
    if user and user.get('password') == password:
        return user
    return None
