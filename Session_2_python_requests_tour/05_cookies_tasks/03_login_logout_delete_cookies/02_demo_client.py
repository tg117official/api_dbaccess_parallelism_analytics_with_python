import requests

session = requests.Session()

# Step 1: Login (POST)
login_data = {
    "username": "sandeep",
    "password": "password123"
}
login_response = session.post("http://localhost:5000/login", data=login_data)
print("Login Response:", login_response.text)

# Step 2: Access Protected Resource
protected_response = session.get("http://localhost:5000/protected")
print("Protected Response After Login:", protected_response.text)

# Step 3: Logout (deletes the cookie)
logout_response = session.get("http://localhost:5000/logout")
print("Logout Response:", logout_response.text)

# Step 4: Try Accessing Protected Again
protected_after_logout = session.get("http://localhost:5000/protected")
print("Protected Response After Logout:", protected_after_logout.text)
