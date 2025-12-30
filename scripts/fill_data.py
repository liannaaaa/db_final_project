import requests

BASE_URL = "http://127.0.0.1:8000"

for i in range(10):
    requests.post(f"{BASE_URL}/athletes", json={
        "full_name": f"Athlete {i}",
        "country": "ARM",
        "birth_year": 1995,
        "wins_count": i
    })
