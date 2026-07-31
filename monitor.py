import requests
from bs4 import BeautifulSoup

URL = "https://hiring.amazon.com/locations/las-vegas-jobs"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=headers, timeout=30)

print("Status code:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

text = soup.get_text(" ", strip=True)

print("Page length:", len(text))

if "warehouse" in text.lower():
    print("Amazon warehouse keywords found")
else:
    print("No warehouse keyword found")
