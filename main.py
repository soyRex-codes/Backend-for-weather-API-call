import os
from dotenv import load_dotenv

import datetime as dt
import requests
import json

load_dotenv(".env")
API_key = os.environ.get("API_key")

# First, get coordinates for the city
BASE_URL = (f"https://api.openweathermap.org/data/2.5/weather?lat={37.20198429798417}&lon={-93.29383269724939}&appid={API_key}")
weather_response = requests.get(BASE_URL).json()
print(json.dumps(weather_response, indent = 2))