import requests
from bs4 import BeautifulSoup
import json
import os

URLS = [
    "https://hiring.amazon.com/locations/las-vegas-jobs",
    "https://hiring.amazon.com/locations/north-las-vegas-jobs"
]

STATE_FILE = "jobs_seen.json"

headers = {
    "User-Agent": "Mozilla/5.0"
}

current_jobs = set()

for url in URLS:
    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Collect text that may contain job listings
        for item in soup.find_all(["a", "div", "span", "h2", "h3"]):
            text = item.get_text(" ", strip=True)

            if any(word in text.lower() for word in [
                "warehouse",
                "fulfillment",
                "associate",
                "sortation",
                "delivery station"
            ]):
                if len(text) > 20:
                    current_jobs.add(text)

    except Exception as e:
        print(f"Error checking {url}: {e}")


if os.path.exists(STATE_FILE):
    with open(STATE_FILE, "r") as f:
        old_jobs = set(json.load(f))
else:
    old_jobs = set()


new_jobs = current_jobs - old_jobs

if new_jobs:
    print("NEW AMAZON JOBS FOUND:")
    for job in new_jobs:
        print("-", job)
else:
    print("No new jobs found.")


with open(STATE_FILE, "w") as f:
    json.dump(list(current_jobs), f, indent=2)
