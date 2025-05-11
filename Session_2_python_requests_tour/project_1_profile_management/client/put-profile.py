import requests

updates = [
    {
        "id": 1,
        "name": "John Doe Updated",
        "email": "john_updated@example.com",
        "skills": ["Flask", "FastAPI"],
        "resume": "https://example.com/resume1_updated.pdf"
    },
    {
        "id": 2,
        "name": "Jane Smith Updated",
        "email": "jane_updated@example.com",
        "skills": ["ML", "AI"],
        "resume": "https://example.com/resume2_updated.pdf"
    },
    {
        "id": 3,
        "name": "Alice Patel Updated",
        "email": "alice_updated@example.com",
        "skills": ["Big Data", "ETL"],
        "resume": "https://example.com/resume3_updated.pdf"
    }
]

for u in updates:
    res = requests.put(f"http://localhost:5000/profiles/{u['id']}", json=u)
    print(f"Updated {u['id']}:", res.json())
