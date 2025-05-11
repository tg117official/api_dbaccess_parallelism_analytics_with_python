import requests
import json

# API base URL for user with ID = 2
url = "https://reqres.in/api/users/2"

# API Key Header
headers = {
    "x-api-key": "reqres-free-v1"
}

# ----------------------------------------
# STEP 1: GET existing user data (before deletion)
# ----------------------------------------
get_response = requests.get(url, headers=headers)
original_data = get_response.json().get("data")

print("User Data Before DELETE:")
print(json.dumps(original_data, indent=4))
print()

# ----------------------------------------
# STEP 2: Send DELETE request
# ----------------------------------------
delete_response = requests.delete(url, headers=headers)
print("DELETE Status Code:", delete_response.status_code)
print("Was DELETE request successful?", delete_response.ok)
print()

# ----------------------------------------
# STEP 3: Try GET again to simulate "after delete"
# (Note: since this is a mock API, the resource still exists)
# ----------------------------------------
get_response_after = requests.get(url, headers=headers)
after_delete_data = get_response_after.json().get("data")

print("User Data After DELETE (Mock API — still available):")
print(json.dumps(after_delete_data, indent=4))
