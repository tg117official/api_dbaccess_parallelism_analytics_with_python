import requests

# Use a session to persist cookies
session = requests.Session()

# STEP 1: Set cookies (GET)
print("Visiting /set_cookies to set various cookies...")
set_url = "http://localhost:5000/set_cookies"
set_response = session.get(set_url)
print("Response:", set_response.text)

# STEP 2: View all cookies that the client now has
print("\nCookies Stored in Session:")
for cookie in session.cookies:
    print(f"{cookie.name} = {cookie.value}")

# STEP 3: Access general endpoint
print("\nAccessing /show_cookies:")
show_response = session.get("http://localhost:5000/show_cookies")
print(show_response.json())

# STEP 4: Access path-restricted endpoint
print("\nAccessing /only_here:")
only_here_response = session.get("http://localhost:5000/only_here")
print(only_here_response.json())
