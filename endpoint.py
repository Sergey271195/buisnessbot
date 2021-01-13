import requests

BASE_URL = "https://xn--37-9kcqjffxnf3b.xn--p1ai"

req = requests.get(f"{BASE_URL}/api/bot/getServices.php?subsection=181")
print(req.json())