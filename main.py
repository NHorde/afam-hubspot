# Local
import os
import json

# 3rd Party
from dotenv import load_dotenv
import requests


# Load environment
load_dotenv()


API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")

headers = {}

url = f"{API_URL}/crm/v3/properties/Contact"

querystring = {
    "archived": "false",
    "hapikey": API_KEY
}

headers = {'accept': 'application/json'}

response = requests.request(
    method="GET",
    url=url,
    headers=headers,
    params=querystring
)

response = response.json()

print(json.dumps(response, indent=3))



