import requests
import re

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

    location_lower = location.lower()

    # Only accept actual Nevada locations
    is_nevada = (
        "las vegas" in location_lower
        or "north las vegas" in location_lower
        or "nv," in location_lower
        or ", nv" in location_lower
        or "nevada" in location_lower
    )

    is_warehouse = any(word in title.lower() for word in [
        "warehouse",
        "fulfillment",
        "sortation",
        "delivery station",
        "associate"
    ])

    if is_nevada and is_warehouse:
        matches.append(job)

print("Las Vegas warehouse matches:", len(matches))

for job in matches:
    print("---")
    print("TITLE:", job.get("title"))
    print("LOCATION:", job.get("location"))
    print("ID:", job.get("id"))
