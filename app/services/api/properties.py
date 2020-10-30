# Python
import os
from libs.constants import PROPERTIES_VIEW

# 3rd Party
import requests

# Local
from libs.state import State
from libs.logger import BASE_LOGGER
logger = BASE_LOGGER.getChild(__name__)

def request_properties_api(state: State):
    """
    Properties API

    :param state:
    :type state:
    :return:
    :rtype:
    """
    API_KEY = os.getenv("API_KEY")
    API_URL = os.getenv("API_URL")

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

    return parse_request(state=state, response = response.json())

def parse_request(state: State, response: str):
    """
    Parsing properties API

    :param state:
    :type state:
    :param response: string
    :type response: string
    :return:
    :rtype:
    """
    for result in response["results"]:
        # print(result["label"])
        if result["name"] in PROPERTIES_VIEW:
            print(result["name"])
