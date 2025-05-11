# client.py

import requests

# --- GET Request ---
response = requests.get('http://127.0.0.1:5000/greet', params={'name': 'John'})
print("GET Response:", response.json())

# --- POST Request ---
data = {
    'num1': 5,
    'num2': 7
}
response1 = requests.post('http://127.0.0.1:5000/add', json=data)

response2 = requests.post('http://127.0.0.1:5000/multiply', json=data)
# http://127.0.0.1:5000/multiply?num1=5&num2=7


print("POST Response:", response.json())
print("POST Response:", response1.json())
print("POST Response:", response2.json())