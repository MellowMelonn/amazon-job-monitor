import requests

URL = "https://www.amazon.jobs/en/search.json"

headers = {
    "User-Agent": "Mozilla/5.0"
}

params = {
    "base_query": "warehouse associate",
    "result_limit": 100
}

response = requests.get(URL, headers=headers, params=params, timeout=30)

print("Status code:", response.status_code)

data = response.json()

jobs = data.get("jobs", [])

print("Total jobs returned:", len(jobs))

matches = []

for job in jobs:
    title = job.get("title", "")
    location = job.get("location", "")

    combined = f"{title} {location}".lower()

    if (
        any(place in combined for place in [
            "las vegas",
            "north las vegas",
            "nv",
            "nevada"
        ])
        and
        any(word in combined for word in [
            "warehouse",
            "fulfillment",
            "associate",
            "sortation",
            "delivery station"
        ])
    ):
        matches.append(job)

print("Las Vegas warehouse matches:", len(matches))

for job in matches:
    print("---")
    print("TITLE:", job.get("title"))
    print("LOCATION:", job.get("location"))
    print("ID:", job.get("id"))
