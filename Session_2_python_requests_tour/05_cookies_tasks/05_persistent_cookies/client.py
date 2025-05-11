import requests

# Use a session to simulate browser-like behavior
session = requests.Session()

# Toggle remember_me here
remember_me = True

# Login with or without 'remember me'
login_data = {
    "username": "sandeep",
    "password": "password123",
    "remember_me": "true" if remember_me else "false"
}
login_response = session.post("http://localhost:5000/login", data=login_data)
print("Login Response:", login_response.text)

# Print stored cookies
print("\nStored Cookies:")
for cookie in session.cookies:
    print(f"{cookie.name} = {cookie.value}, expires = {cookie.expires}")

# Access protected route
protected = session.get("http://localhost:5000/protected")
print("\nProtected Response:", protected.text)

# Logout
logout = session.get("http://localhost:5000/logout")
print("\nLogout Response:", logout.text)

# Access again after logout
protected_after_logout = session.get("http://localhost:5000/protected")
print("\nProtected After Logout:", protected_after_logout.text)
