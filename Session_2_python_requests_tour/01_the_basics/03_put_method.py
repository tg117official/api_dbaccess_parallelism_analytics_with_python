## What is the PUT Method?

## Purpose :

# The `PUT` method is used to update or replace an existing resource on the server.
# If the resource does not exist, some servers may choose to create it.
# Idempotent: Multiple identical PUT requests will have the same effect as one.


## Common Use Case:

# Imagine you have a user profile:

# {
#   "id": 101,
#   "name": "Alice",
#   "role": "DataScientist"
# }


# You want to update the role from `"DataScientist"` to `"ML Engineer"`.
# You send a PUT request with the updated JSON payload.
# The server replaces the entire profile with the new one.


import requests
import json

# API endpoint
url = "https://reqres.in/api/users/2"

# Replace with your actual API key after signup
api_key = "reqres-free-v1"

# Headers including Authorization
headers = {
    "x-api-key": "reqres-free-v1"
}

# Data to update
updated_data = {
    "name": "Alice",
    "job": "ML Engineer"
}

# Send PUT request
response = requests.put(url, headers=headers, json=updated_data)

# Show status
print("Status Code:", response.status_code)
print("Was the request successful?", response.ok)
print()

# Show headers
print("Response Headers:")
print(response.headers)
print()

# JSON response
response_json = response.json()
print("JSON Response from Server:")
print(json.dumps(response_json, indent=4))




## Tips:

# Idempotency : run the same script twice → same output.
# unlike `PATCH`, `PUT` replaces the entire object, not part of it.



### Bonus Example for Explanation:

# | Method | Use Case                            | Behavior                              |
# | ------ | ----------------------------------- | ------------------------------------- |
# | GET    | Fetch user profile                  | Only retrieves data                   |
# | POST   | Create a new user                   | Creates new resource                  |
# | PUT    | Replace user profile                | Replaces entire resource (idempotent) |
# | PATCH  | Update only "role" field in profile | Modifies part of resource             |
# | DELETE | Remove user                         | Deletes the resource                  |
