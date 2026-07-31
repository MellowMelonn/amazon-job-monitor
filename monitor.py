import requests
import json

URL = "https://www.amazon.jobs/en/search.json?base_query=&loc_query=Las%20Vegas%2C%20NV"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=headers, timeout=30)

print("Status code:", response.status_code)

data = response.json()

jobs = data.get("jobs", [])

print("Jobs found:", len(jobs))

for job in jobs[:10]:
    print(job.get("title"))
    print(job.get("location"))
    print(job.get("url"))
    print("---")
