from services.file_utils import load_json, write_json

USER_FILE = r"C:\Users\Sandeep\PycharmProjects\Python_APIs_and_DB_access\Session_2_python_requests_tour\ecom_project\data\users.json"

def update_user(username, updated_data):
    users = load_json(USER_FILE)
    for user in users:
        if user['username'] == username:
            user['email'] = updated_data.get('email', user['email'])
            user['password'] = updated_data.get('password', user['password'])
            break
    write_json(USER_FILE, users)
