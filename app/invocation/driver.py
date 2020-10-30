"""
Invocation
"""

# Python
import os
import json

# Local
import setup
from libs.state import State
from libs.logger import BASE_LOGGER


# 3rd Party
from dotenv import load_dotenv
import requests


# Load environment
load_dotenv()

# Activate logger
logger = BASE_LOGGER.getChild(__name__)

def invoke(state: State):
    print(state)
    exit(1)
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

    # print(json.dumps(response, indent=3))

    print(response["results"][0])


if __name__ == "__main__":
    invoke(state = State())