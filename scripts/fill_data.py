import requests

URL = "http://127.0.0.1:8000/athletes"

for i in range(30):
    requests.post(URL, json={
        "full_name": f"Athlete {i}",
        "country": "ARM" if i % 2 == 0 else "USA",
        "birth_year": 1990 + i % 10,
        "wins_count": i,
        "profile": {
            "height": 170 + i,
            "weight": 65 + i,
            "achievements": ["champion", "record"]
        }
    })
