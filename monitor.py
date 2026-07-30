import requests
from bs4 import BeautifulSoup
import hashlib
import os

URLS = [
    "https://hiring.amazon.com/locations/las-vegas-jobs",
    "https://hiring.amazon.com/locations/north-las-vegas-jobs"
]

text = ""

headers = {
    "User-Agent": "Mozilla/5.0"
}

for url in URLS:
    try:
        r = requests.get(url, headers=headers, timeout=30)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        text += soup.get_text(" ", strip=True)
    except Exception as e:
        print(f"Error checking {url}: {e}")

print(hashlib.sha256(text.encode()).hexdigest())
