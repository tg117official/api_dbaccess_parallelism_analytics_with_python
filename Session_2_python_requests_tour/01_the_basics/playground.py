## Demo Script for PUT Method

import requests
import json

# ----------------------------------------
# STEP 1: Define the API endpoint for PUT
# ----------------------------------------
url = "https://httpbin.org/put"

# ----------------------------------------
# STEP 2: Create a sample "existing" resource
# ----------------------------------------
original_data = {
    "id": 101,
    "name": "Alice",
    "role": "DataScientist",
    "batch": "March2025"
}

print("Original Data Sent via PUT (simulated update):")
print(json.dumps(original_data, indent=4))
print()

# ----------------------------------------
# STEP 3: Send PUT request to update/replace the resource
# ----------------------------------------
response = requests.put(url, json=original_data)

# ----------------------------------------
# STEP 4: Print HTTP response metadata
# ----------------------------------------
print("Status Code:", response.status_code)
print("Request Successful?", response.ok)
print()

# ----------------------------------------
# STEP 5: Raw response content
# ----------------------------------------
print("Response Headers:")
print(response.headers)
print()

# ----------------------------------------
# STEP 6: Print entire response as string
# ----------------------------------------
print("Response Text:")
print(response.text)
print()

# ----------------------------------------
# STEP 7: Parse and display JSON response
# ----------------------------------------
response_json = response.json()

print("SON Parsed Response:")
print(json.dumps(response_json, indent=4))
print()

# ----------------------------------------
# STEP 8: Extract and show what server received
# ----------------------------------------
print("JSON Received by Server (from client):")
print(json.dumps(response_json.get('json'), indent=4))