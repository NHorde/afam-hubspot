# Python
import os

# 3rd Party
import requests

# Local
from libs.state import State
from libs.logger import BASE_LOGGER
logger = BASE_LOGGER.getChild(__name__)

def request_properties_api(state: State):

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