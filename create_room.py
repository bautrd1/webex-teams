import requests
import json
from pprint import pprint

token = "MDhmMDRmMDUtOGE4YS00MjY3LWE1MDEtYjFiMmRjMTA5NDM2NWY0ZjEwZDMtNDVh_P0A1_ebee85b6-002e-44c5-8392-ccef6152c511"
BASE_URL = "https://webexapis.com"
room = "v1/rooms"

body = {'title': "Sheldons Room"}
headers = {
    'Authorization': f"Bearer {token}",
    'Content-Type': "application/json"
}

room_url = f"{BASE_URL}/{room}"
resp = requests.post(room_url, headers=headers, data=json.dumps(body))
pprint(resp.json(), indent=4)
