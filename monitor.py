import requests

URL = "https://www.amazon.jobs/en/search.json"

headers = {
    "User-Agent": "Mozilla/5.0"
}

params = {
    "base_query": "warehouse associate",
    "loc_query": "Las Vegas Nevada",
    "result_limit": 50
}

response = requests.get(URL, headers=headers, params=params, timeout=30)

print("Status code:", response.status_code)

data = response.json()

jobs = data.get("jobs", [])

print("Total jobs returned:", len(jobs))

found = 0

for job in jobs:
    title = job.get("title", "")
    location = job.get("location", "")

    combined = f"{title} {location}".lower()

    if (
        ("nv" in combined or "nevada" in combined or "las vegas" in combined)
        and
        any(word in combined for word in [
            "warehouse",
            "fulfillment",
            "associate",
            "sortation",
            "delivery station"
        ])
    ):
        found += 1
        print("---")
        print("TITLE:", title)
        print("LOCATION:", location)
        print("ID:", job.get("id"))

print("Matching Las Vegas warehouse jobs:", found)
