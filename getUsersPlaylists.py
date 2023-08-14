import json
import base64
import requests

def get_credential(key) :
    try: 
        with open("configs/credential.json", "r") as file :
            credential = json.load(file)
            return credential[key]
    except FileNotFoundError:
        return None

client_id = get_credential("ID")
client_secret = get_credential("SECRETS")
user_id = get_credential("USER_ID")

def read_AccessToken_to_file():
    with open("configs/AuthToken.txt", "r") as file:
        token = file.read()
        return token

access_token = read_AccessToken_to_file()

url = f"https://api.spotify.com/v1/users/{user_id}/playlists"
header = {
    'Authorization': 'Bearer ' + access_token
}

response = requests.get(url,headers=header)
response_json = response.json()

with open("db/usersplaylists.json", "w") as file :
    json.dump(response_json,file,indent=4)