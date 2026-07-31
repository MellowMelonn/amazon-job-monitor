import requests

SEARCHES = [
    "Las Vegas, NV",
    "North Las Vegas, NV"
]

headers = {
    "User-Agent": "Mozilla/5.0"
}

for location in SEARCHES:
    url = (
        "https://www.amazon.jobs/en/search.json"
        f"?base_query=warehouse"
        f"&loc_query={location.replace(' ', '%20')}"
    )

    print("\nSearching:", location)

    response = requests.get(url, headers=headers, timeout=30)

    print("Status code:", response.status_code)

    data = response.json()

    jobs = data.get("jobs", [])

    print("Jobs found:", len(jobs))

    for job in jobs[:10]:
        title = job.get("title")
        loc = job.get("location")
        job_id = job.get("id")

        print("---")
        print(title)
        print(loc)
        print("ID:", job_id)
