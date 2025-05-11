import requests
import json

# ----------------------------------------
# STEP 1: Define the endpoint (httpbin echoes headers back)
# ----------------------------------------
url = "https://httpbin.org/headers"

# ----------------------------------------
# STEP 2: Define custom headers to send in the request
# ----------------------------------------
custom_headers = {
    "User-Agent": "MyCustomClient/1.0",
    "x-api-key": "dummy-api-key-123",
    "Accept": "application/json",
    "Authorization": "Bearer test-token-abc"
}

print("Headers Being Sent to Server:")
print(json.dumps(custom_headers, indent=4))
print()

# ----------------------------------------
# STEP 3: Send the GET request with custom headers
# ----------------------------------------
response = requests.get(url, headers=custom_headers)

# ----------------------------------------
# STEP 4: Check the status code
# ----------------------------------------
print("HTTP Status Code:", response.status_code)
print("Request Successful?", response.ok)
print()

# ----------------------------------------
# STEP 5: View the headers as seen by the server (httpbin echoes them back)
# ----------------------------------------
print("Headers Received by Server (Echoed Back):")
server_view = response.json().get("headers")
print(json.dumps(server_view, indent=4))
print()

# ----------------------------------------
# STEP 6: View the response headers sent by httpbin.org
# ----------------------------------------
print("Response Headers from Server:")
print(json.dumps(dict(response.headers), indent=4))
print()

# ----------------------------------------
# STEP 7: Explore specific headers from the response
# ----------------------------------------
print("Explanation of Key Response Headers:")
print("Content-Type      ➤ Type of response content (e.g., application/json)")
print("Content-Length    ➤ Size of the response body in bytes")
print("Date              ➤ Time when the server generated the response")
print("Server            ➤ Server software name")
print("Access-Control-*  ➤ CORS-related headers for browser-based access")

