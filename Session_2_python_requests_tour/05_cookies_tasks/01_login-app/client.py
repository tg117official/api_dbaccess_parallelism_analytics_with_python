import requests

# 1. POST Login Request
login_url = "http://localhost:5000/login"
login_data = {
    "username": "sandeep",
    "password": "password123"
}
login_response = requests.post(login_url, data=login_data)

# Check login status
print("Login Response:", login_response.text)

# 2. Extract and send cookies manually
cookies = login_response.cookies

# 3. Access protected resource with cookies
protected_url = "http://localhost:5000/protected"
protected_response = requests.get(protected_url, cookies=cookies)

print("Protected Response:")
print(protected_response.text)
