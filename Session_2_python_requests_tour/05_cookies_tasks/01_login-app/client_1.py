import requests

# Create a session object
session = requests.Session()

# 1. Login using session (automatically stores cookies)
login_data = {
    "username": "sandeep",
    "password": "password123"
}
session.post("http://localhost:5000/login", data=login_data)

# 2. Access protected route without manually handling cookies
protected_response = session.get("http://localhost:5000/protected")
print("Protected Response Using Session:")
print(protected_response.text)
