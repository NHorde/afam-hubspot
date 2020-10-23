# Local
import os

#3rd Party
from dotenv import load_dotenv
import requests

# Load environment
load_dotenv()

# https://pypi.org/project/hubspot-api-client/


API_KEY = os.getenv("API_KEY")
API_URL = f"{os.getenv('API_URL')}/crm/v3/objects/contacts"


properties = "email, firstname, lastname, alumni, donation, expertise, shasta_employer," \
             " shasta_grant, shasta_mentor, shasta_intern"

querystring = {
    "limit": "100",
    "properties": properties,
    "paginateAssociations": "false",
    "archived": "false",
    "hapikey": API_KEY
}
headers = {'accept': 'application/json'}

response = requests.request("GET", url=API_URL, headers=headers, params=querystring)
print(response.text.encode('utf-8'))

exit(1)
# 2nd page
querystring = {"after":"2606","limit":"100","properties":properties,"paginateAssociations":"false","archived":"false","hapikey":MY_HUBSPOT_API_KEY}

response = requests.request("GET", url, headers=headers, params=querystring)
response.encoding = "utf-8"
print
print(response.text.encode('utf-8'))

# Companies
url = "https://api.hubapi.com/crm/v3/objects/companies"
properties="name,domain,city,state,country,industry,phone_number,description"
querystring = {"limit":"100","properties":properties,"paginateAssociations":"false","archived":"false","hapikey":MY_HUBSPOT_API_KEY}
response = requests.request("GET", url, headers=headers, params=querystring)
response.encoding = "utf-8"
print
print(response.text.encode('utf-8'))