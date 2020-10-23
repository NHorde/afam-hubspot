# Local
import os

#3rd Party
from dotenv import load_dotenv

# Load environment
load_dotenv()

API_KEY = os.getenv("APIKEY")

client = Hubspot3(api_key=API_KEY)
all_companies = client.companies.get_all()

print(all_companies)