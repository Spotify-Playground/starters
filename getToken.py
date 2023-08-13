import requests

import os 
import json

credential_path = os.path.join("./configs","credential.json")
with open(credential_path) as f :
    credential = json.load(f)

CLIENT_ID = credential["ID"]
CLIENT_SECRETS = credential["SECRETS"]

url = "https://accounts.spotify.com/api/token"
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}
data = {
    "grant_type": "client_credentials",
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRETS
}

response = requests.post(url, headers=headers, data=data)

if response.status_code == 200:
    response_json = response.json()
else:
    print(f"Error: {response.status_code}")

if "access_token" in response_json:
    access_token = response_json["access_token"]
    print(f"Value of 'access_token': {access_token}")
else:
    print("Key 'access_token' not found in the JSON response.")