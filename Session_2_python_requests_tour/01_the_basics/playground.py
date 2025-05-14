import requests

print("7. Handling delayed response with timeout:")
try:
    # This endpoint simulates delay in response (5 seconds)
    timeout_response = requests.get("https://httpbin.org/delay/5", timeout=3)
    print("Timeout Response:", timeout_response.text)
except requests.exceptions.Timeout:
    print("Request timed out after 3 seconds")
print("\n")