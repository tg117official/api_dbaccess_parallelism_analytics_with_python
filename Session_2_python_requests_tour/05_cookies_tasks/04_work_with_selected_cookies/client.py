import requests

# Step 1: Hit the endpoint to set cookies
session = requests.Session()
session.get("http://localhost:5000/set_cookies")

print("All Cookies in Session:")
for cookie in session.cookies:
    print(f"{cookie.name} = {cookie.value}")

# Step 2: Send only the 'user' cookie back manually
selected_cookie = {
    "user": session.cookies.get("user")  # selectively pick 'user' cookie
}
response = requests.get("http://localhost:5000/read_selected_cookie", cookies=selected_cookie)

print("\nResponse After Sending Only 'user' Cookie:")
print(response.text)
