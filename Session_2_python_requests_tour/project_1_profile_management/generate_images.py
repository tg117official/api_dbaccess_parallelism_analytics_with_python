import requests
import os

def download_image(url, filename):
    os.makedirs("images", exist_ok=True)
    path = os.path.join("images", filename)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(path, "wb") as f:
                f.write(response.content)
            print(f"Saved: {path}")
        else:
            print(f"Failed ({response.status_code}): {url}")
    except Exception as e:
        print(f"Error: {e}")

# Fetch profiles
response = requests.get("http://localhost:5000/profiles")
profiles = response.json()

# Download images
for profile in profiles:
    name_for_url = profile["name"].replace(" ", "+")
    file_name = f"{profile['id']}_{profile['name'].replace(' ', '_')}.jpg"
    image_url = f"https://dummyimage.com/150x150/0000ff/ffffff&text={name_for_url}"
    download_image(image_url, file_name)
