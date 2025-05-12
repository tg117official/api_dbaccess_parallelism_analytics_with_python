# client/register_user.py

import requests

API_URL = "http://localhost:5000/register"

def register_user():
    user_data = {
        "username": "sandeep",
        "password": "secure123",
        "email": "sandeep@example.com"
    }

    try:
        response = requests.post(API_URL, json=user_data)

        if response.status_code == 201:
            print("Registration successful.")
        elif response.status_code == 409:
            print("Username already exists.")
        else:
            print(f"Registration failed. Status code: {response.status_code}")
            print(response.text)
    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    register_user()
