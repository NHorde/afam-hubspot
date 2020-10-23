# https://pypi.org/project/hubspot-api-client/
import requests

url = "https://api.hubapi.com/crm/v3/objects/contacts"

MY_HUBSPOT_API_KEY = "bf54b079-40a6-47ff-87e6-015337af7966"
properties="email,firstname,lastname,alumni,donation,expertise,shasta_employer,shasta_grant,shasta_mentor,shasta_intern"

querystring = {"limit":"100","properties":properties,"paginateAssociations":"false","archived":"false","hapikey":MY_HUBSPOT_API_KEY}
headers = {'accept': 'application/json'}

response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text.encode('utf-8'))

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