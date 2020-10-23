# Local
import os

#3rd Party
from dotenv import load_dotenv

# Load environment
load_dotenv()

key = os.getenv("APIKEY")

print(key)