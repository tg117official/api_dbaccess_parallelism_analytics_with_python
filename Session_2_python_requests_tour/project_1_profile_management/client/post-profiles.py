import requests

profiles = [
    {
        "name": "Alice Patel",
        "email": "alice@example.com",
        "skills": ["API", "Data Analysis"],
        "resume": "https://example.com/resume3.pdf"
    },
    {
        "name": "Bob Kumar",
        "email": "bob@example.com",
        "skills": ["DevOps", "CI/CD"],
        "resume": "https://example.com/resume4.pdf"
    },
    {
        "name": "Carlos Mendes",
        "email": "carlos@example.com",
        "skills": ["React", "Node.js"],
        "resume": "https://example.com/resume5.pdf"
    }
]

for profile in profiles:
    res = requests.post("http://localhost:5000/profiles", json=profile)
    print("Created:", res.json())
