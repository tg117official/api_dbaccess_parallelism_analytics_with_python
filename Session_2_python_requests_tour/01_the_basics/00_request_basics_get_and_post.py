# ---------------------------------------
# Title: Exploring requests.get() and request.post() in Python
# Objective: Demonstrate how to work with GET requests and response objects
# URLs used: https://xkcd.com/, https://imgs.xkcd.com/comics/decay_chain.png
# ---------------------------------------

import requests

# -----------------------------
# Step 1: Send a GET request to a webpage
# -----------------------------

url1 = "https://xkcd.com/"
response = requests.get(url1)

# Step 1 : Use dir() to explore available attributes and methods of the response object
print("Attributes and Methods of response object:")
print(dir(response))  # Helps see what operations we can perform
print("\n")

# -----------------------------
# Step 2: Use help() on response object to understand its purpose
# -----------------------------
# Uncomment the line below if you're running this in an interactive environment like a Jupyter Notebook or Python shell
# help(response)

# -----------------------------
# Step 3: Use response.text to get the content of the web page as a string
# -----------------------------
print("HTML content using response.text (first 500 characters):")
print(response.text[:500])  # Displaying first 500 characters to keep output short
print("\n")

# -----------------------------
# Step 4: Check the status code and status of the request
# -----------------------------
print("Status Code:", response.status_code)  # 200 means OK
print("Was the request successful?", response.ok)  # True if status_code is 200–399
print("\n")

# -----------------------------
# Step 5: Check the response headers
# -----------------------------
print("Response Headers:")
for key, value in response.headers.items():
    print(f"{key}: {value}")
print("\n")

# -----------------------------
# Step 6: GET an image (binary content)
# -----------------------------
url2 = "https://imgs.xkcd.com/comics/decay_chain.png"
img_response = requests.get(url2)

# Use .content to access the raw binary content of the image
print("Binary Content of the image (first 100 bytes):")
print(img_response.content[:100])
print("\n")

# -----------------------------
# Step 7: Download and save the image locally
# -----------------------------
with open("downloaded_image.png", "wb") as f:
    f.write(img_response.content)
print("Image successfully downloaded as 'downloaded_image.png'")

# -----------------------------
# Recap (for discussion)
# - Used GET request to fetch web page and image
# - Used dir(), help() to explore response object
# - Used response.text for HTML and response.content for binary image
# - Checked status_code, ok, and headers
# -----------------------------




# Advanced Usage of the requests Module in Python
# URL Used: https://httpbin.org/
# ------------------------------------------

import requests

# -----------------------------
# Step 1: Pass parameters using URL itself
# -----------------------------
print("\n1. GET request with parameters in URL manually:")
manual_url = "https://httpbin.org/get?name=John&city=Delhi"
response_manual = requests.get(manual_url)
print("URL Sent:", response_manual.url)
print("Response JSON:")
print(response_manual.json())
print("\n")

# -----------------------------
# Step 2: Pass parameters using 'params' argument (recommended way)
# -----------------------------
print("2. GET request with params using 'params' argument:")
payload = {'name': 'Alice', 'city': 'Mumbai'}
response_params = requests.get("https://httpbin.org/get", params=payload)
print("URL Sent:", response_params.url)  # Shows full URL with encoded query params
print("Response JSON:")
print(response_params.json())
print("\n")

# -----------------------------
# Step 3: POST request to send form data
# -----------------------------
print("3. POST request with form data:")
form_data = {'username': 'admin', 'password': '1234'}
post_response = requests.post("https://httpbin.org/post", data=form_data)
print("Response JSON:")
post_json = post_response.json()  # Convert response to dictionary
print(post_json)
print("\n")

# -----------------------------
# Step 4: Extracting specific content from response JSON
# -----------------------------
print("4. Extracting form data from the JSON dictionary:")
print("Form Data Received by Server:")
print(post_json['form'])  # This shows what was sent in the form
print("\n")

# -----------------------------
# Step 5: Basic Authentication using requests.get and auth parameter
# -----------------------------
print("5. Basic Authentication (username: user, password: pass):")
auth_response = requests.get("https://httpbin.org/basic-auth/user/pass", auth=('user', 'pass'))
print("Status Code:", auth_response.status_code)
print("Authenticated Response:", auth_response.json() if auth_response.ok else "Authentication failed")
print("\n")

# -----------------------------
# Step 6: Form-based authentication (handled just like any POST request)
# -----------------------------
print("6. Form-based Authentication (simulated):")
login_data = {'username': 'user1', 'password': 'mypassword'}
form_auth_response = requests.post("https://httpbin.org/post", data=login_data)
print("Posted Login Form Data:")
print(form_auth_response.json()['form'])
print("\n")

# -----------------------------
# Step 7: Handling delays with the timeout parameter
# -----------------------------
print("7. Handling delayed response with timeout:")
try:
    # This endpoint simulates delay in response (5 seconds)
    timeout_response = requests.get("https://httpbin.org/delay/5", timeout=3)
    print("Timeout Response:", timeout_response.text)
except requests.exceptions.Timeout:
    print("Request timed out after 3 seconds")
print("\n")

# -----------------------------
# Recap:
# - GET with manual and params argument
# - POST with form data
# - JSON response and dictionary extraction
# - Basic and form authentication
# - Handling timeouts
# -----------------------------

