import requests
import json
import os

URL = "https://www.amazon.jobs/en/search.json"

STATE_FILE = "jobs_seen.json"

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

matches = []

for job in jobs:
    title = job.get("title", "")
    location = job.get("location", "")

    location_lower = location.lower()

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
        matches.append({
            "id": job.get("id"),
            "title": title,
            "location": location
        })


if os.path.exists(STATE_FILE):
    with open(STATE_FILE, "r") as f:
        old_jobs = json.load(f)
else:
    old_jobs = []


old_ids = {job["id"] for job in old_jobs}

new_jobs = [
    job for job in matches
    if job["id"] not in old_ids
]


print("Current Las Vegas warehouse jobs:", len(matches))
print("New jobs:", len(new_jobs))


for job in new_jobs:
    print("NEW:")
    print(job["title"])
    print(job["location"])


with open(STATE_FILE, "w") as f:
    json.dump(matches, f, indent=2)
