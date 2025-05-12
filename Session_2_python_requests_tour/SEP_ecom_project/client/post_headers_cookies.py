# client/post_headers_cookies.py

import requests

BASE_URL = "http://localhost:5000"

def send_headers_and_cookies():
    headers = {
        "X-App-Client": "ecom-app-v1",
        "X-Theme": "dark"
    }

    cookies = {
        "preferred_currency": "INR",
        "cart_hint": "show"
    }

    response = requests.get(f"{BASE_URL}/inspect", headers=headers, cookies=cookies)

    print("✅ Headers sent:")
    print(headers)
    print("\n✅ Cookies sent:")
    print(cookies)

    print("\n📄 Server Response:")
    print(response.json())

if __name__ == '__main__':
    send_headers_and_cookies()
