import requests

# Define the endpoint for GET request
url = "https://httpbin.org/get"

# Define the query parameters (sent as part of URL)
params = {
    'name': 'John',
    'role': 'DataEngineer',
    'batch': 'March2025'
}

# 1. Make the GET request with query parameters
response = requests.get(url, params=params)

# 2. Print the full URL generated (for teaching how params are added to URL)
print("Final URL with query parameters:")
print(response.url)
print()

# 3. Print the HTTP status code to check if the request was successful
print("Status Code:")
print(response.status_code)
print()

# Check if the request was successful using .ok
print("Was the request successful?")
print(response.ok)
print()

# 4. Print the headers of the response (useful for authentication/token examples later)
print("Response Headers:")
print(response.headers)
print()

### Header Summary for `https://xkcd.com` Response

# | Header                                   |Meaning                                                         |
# | ---------------------------------------- | ------------------------------------------------------------------- |
# | `Connection: keep-alive`                 | Keeps TCP connection open for reuse.                                |
# | `Content-Length: 2789`                   | Size of the uncompressed response body in bytes.                    |
# | `Server: nginx`                          | Server software handling the request.                               |
# | `Content-Type: text/html; charset=UTF-8` | Response is an HTML document encoded in UTF-8.                      |
# | `ETag: W/"..."`                          | Version identifier for caching/conditional requests.                |
# | `Expires: ...`                           | Time when the cached response becomes stale.                        |
# | `Cache-Control: max-age=300`             | Cache valid for 300 seconds (5 minutes).                            |
# | `Content-Encoding: gzip`                 | Response body is gzip-compressed.                                   |
# | `Accept-Ranges: bytes`                   | Supports partial content requests (e.g., range downloads).          |
# | `Age: 249`                               | Response was cached 249 seconds ago.                                |
# | `Date: ...`                              | Timestamp when response was generated.                              |
# | `Via: 1.1 varnish`                       | Passed through a caching proxy (Varnish).                           |
# | `X-Served-By: ...`                       | Identifies the specific cache server (location hint: BOM = Mumbai). |
# | `X-Cache: HIT`                           | Response was served from cache.                                     |
# | `X-Cache-Hits: 0`                        | First time this cache item was served.                              |
# | `X-Timer: ...`                           | Internal timing for request processing via Varnish.                 |
# | `Vary: Accept-Encoding`                  | Response varies by `Accept-Encoding`; affects cache storage.        |


# 5. Print the raw content (bytes) of the response (for binary data examples)
print("Raw Content:")
print(response.content)
print()

# 6. Print the text content of the response (HTML or plain text)
print("Response Text:")
print(response.text)
print()

# 7. Parse and print JSON response (httpbin returns it as JSON)
print("JSON Response:")
json_data = response.json()
print(json_data)
print()

# 8. Extracting data from JSON (demonstrates how we retrieve useful info)
print("Extracted Data from JSON Response:")
print("Args received by server:", json_data.get('args'))  # Shows what was received