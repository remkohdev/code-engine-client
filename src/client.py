# Assisted by watsonx Code Assistant

import os
import requests

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

BASE_URL = os.getenv("BASE_URL", "http://127.0.0.1:8000")
response = requests.get(f"{BASE_URL}/hello")

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
