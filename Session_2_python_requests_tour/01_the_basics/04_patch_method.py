import requests
import json

# API base URL for user with ID = 2
url = "https://reqres.in/api/users/2"

# API Key header (from reqres signup)
headers = {
    "x-api-key": "reqres-free-v1"
}

# ----------------------------------------
# STEP 1: GET existing user data (simulate "before" view)
# ----------------------------------------
get_response = requests.get(url, headers=headers)
original_data = get_response.json().get("data")

print("Existing User Data (Before PATCH):")
print(json.dumps(original_data, indent=4))
print()

# ----------------------------------------
# STEP 2: Define partial update (PATCH only updates what's given)
# ----------------------------------------
patch_data = {
    "job": "Senior Data Engineer"
}

print("Data to Update via PATCH:")
print(json.dumps(patch_data, indent=4))
print()

# ----------------------------------------
# STEP 3: Send PATCH request
# ----------------------------------------
patch_response = requests.patch(url, headers=headers, json=patch_data)
print("PATCH Status Code:", patch_response.status_code)
print("Was PATCH request successful?", patch_response.ok)
print()

# ----------------------------------------
# STEP 4: Display server response
# ----------------------------------------
patch_response_json = patch_response.json()

print("Server Response After PATCH:")
print(json.dumps(patch_response_json, indent=4))
