import requests
import base64
import json

#토큰 저장하는 함수
def save_token_to_file(token):
    with open("configs/AuthToken.txt", "w") as file:
        file.write(token)
#토큰 불러오는 함수
def read_token_from_file():
    try:
        with open("configs/RefreshToken.txt", "r") as file:
            token = file.read().strip()
            return token
    except FileNotFoundError:
        return None

def get_credential(key) :
    try: 
        with open("configs/credential.json", "r") as file :
            credential = json.load(file)
            return credential[key]
    except FileNotFoundError:
        return None

client_id = get_credential("ID")
client_secret = get_credential("SECRETS")
redirect_uri = get_credential("RED_URI")
state_key = 'spotify_auth_state'

Refresh_token = read_token_from_file()

url = "https://accounts.spotify.com/api/token"
header = {'Authorization': 'Basic ' + base64.b64encode((client_id + ':' + client_secret).encode()).decode()}
data = {
    "grant_type": "refresh_token",
    "refresh_token": Refresh_token 
}

response = requests.post(url,headers=header,data=data)

response_json = response.json()
access_token=response_json["access_token"]
save_token_to_file(access_token)