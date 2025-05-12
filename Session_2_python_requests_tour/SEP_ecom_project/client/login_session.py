# client/login_session.py

import requests

BASE_URL = "http://localhost:5000"

def login_and_get_profile():
    session = requests.Session()

    login_data = {
        "username": "sandeep",
        "password": "secure123"
    }

    # Login
    login_response = session.post(f"{BASE_URL}/login", json=login_data)

    if login_response.status_code == 200:
        print("Login successful.")
    else:
        print("Login failed.")
        return

    # Access protected route with session
    profile_response = session.get(f"{BASE_URL}/profile")

    if profile_response.status_code == 200:
        print("User Profile:")
        print(profile_response.json())
    else:
        print("Failed to retrieve profile. Status code:", profile_response.status_code)

if __name__ == '__main__':
    login_and_get_profile()
