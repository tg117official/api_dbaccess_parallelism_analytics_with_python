import requests

for pid in [4, 5, 6]:
    res = requests.delete(f"http://localhost:5000/profiles/{pid}")
    print(f"Deleted {pid}:", res.json())
