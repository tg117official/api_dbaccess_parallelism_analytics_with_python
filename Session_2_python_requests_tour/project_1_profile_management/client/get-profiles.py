import requests

resp = requests.get("http://localhost:5000/profiles")
print("All Profiles:", resp.json())

for pid in [1, 2]:
    resp = requests.get(f"http://localhost:5000/profiles/{pid}")
    print(f"Profile {pid}:", resp.json())
