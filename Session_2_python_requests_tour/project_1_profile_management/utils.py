import requests
import os

COOKIE_STORE = {"session_token": "abc123xyz"}

#
# def get_custom_headers():
#     ua = UserAgent()
#     headers = {
#         "User-Agent": ua.random,
#         "Accept": "application/json",
#         "X-App-Client": "JobSearchBot/1.0"
#     }
#     return headers
#
#
# def get_session():
#     session = requests.Session()
#     session.cookies.update(COOKIE_STORE)
#     return session
#
#
# def download_logo(url, company):
#     response = requests.get(url)
#     if response.status_code == 200:
#         file_path = f"{company}_logo.jpg"
#         with open(file_path, "wb") as f:
#             f.write(response.content)
#         print(f"Downloaded logo for {company} -> {file_path}")
#     else:
#         print(f"Failed to download logo for {company}.")

def download_image(url, filename):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded: {filename}")
        else:
            print(f"Failed to download {filename}: {response.status_code}")
    except Exception as e:
        print(f"Error downloading {filename}: {e}")
