import requests

# Define the endpoint for the POST request
url = "https://httpbin.org/post"

# Define the data to send (in JSON format)
data = {
    'name': 'John',
    'course': 'REST API with Python',
    'batch': 'March2025'
}

# Make the POST request with JSON data
response = requests.post(url, json=data)

# Print the HTTP status code to check success
print("Status Code:")
print(response.status_code)
print()

# Check if the request was successful
print("Was the request successful?")
print(response.ok)
print()

# Print the headers of the response
print("Response Headers:")
print(response.headers)
print()

# Print the raw content (bytes) of the response
print("Raw Content:")
print(response.content)
print()

# Print the text content of the response
print("Response Text:")
print(response.text)
print()

# Parse the JSON response from the server
print("JSON Response:")
json_data = response.json()
print(json_data)
print()

# Extract the data you sent (echoed back by httpbin.org)
print("Data sent (as received by the server):")
print(json_data.get('json'))  # This should match the 'data' dictionary