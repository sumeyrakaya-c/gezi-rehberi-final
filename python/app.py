from dotenv import load_dotenv
import os
import requests

load_dotenv()

STRAPI_TOKEN = os.getenv("STRAPI_TOKEN")
STRAPI_URL = os.getenv("STRAPI_URL")

headers = {
    "Authorization": f"Bearer {STRAPI_TOKEN}"
}

response = requests.get(
    f"{STRAPI_URL}/api/cities",
    headers=headers
)

print("Durum kodu:", response.status_code)
print(response.json())