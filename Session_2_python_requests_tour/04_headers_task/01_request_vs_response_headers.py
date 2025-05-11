import requests
import json

# ----------------------------------------
# STEP 1: Define the endpoint (httpbin will echo headers)
# ----------------------------------------
url = "https://httpbin.org/headers"

# ----------------------------------------
# STEP 2: Define custom request headers
# ----------------------------------------
custom_request_headers = {
    "User-Agent": "MyLearningApp/1.0",
    "Accept": "application/json",
    "Authorization": "Bearer test-token-123"
}

# ----------------------------------------
# STEP 3: Send the GET request with custom headers
# ----------------------------------------
response = requests.get(url, headers=custom_request_headers)

# ----------------------------------------
# STEP 4: Display headers sent in the request
# (httpbin returns this in JSON → "headers" field)
print("Headers Sent in the Request (Client ➜ Server):")
print(json.dumps(custom_request_headers, indent=4))
print()

# Confirm using what httpbin server saw:
print("What the Server Received (Echoed Back):")
echoed_request_headers = response.json().get("headers")
print(json.dumps(echoed_request_headers, indent=4))
print()

# ----------------------------------------
# STEP 5: Display headers received in the response
print("Headers Received in the Response (Server ➜ Client):")
print(json.dumps(dict(response.headers), indent=4))
print()

# ----------------------------------------
# STEP 6: Explain the difference
print("Difference Between Request and Response Headers:")
print("- Request Headers are sent FROM client TO server.")
print("- Response Headers are sent FROM server TO client.")
print("- Request headers often include: Authorization, User-Agent, Accept, etc.")
print("- Response headers include metadata like Content-Type, Content-Length, Server, Date, etc.")
print("- Only response headers can include Set-Cookie and caching policies.")
