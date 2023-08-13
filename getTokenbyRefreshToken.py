import requests
import config.info as info
import base64

client_id = info.id
client_secret = info.secret

#토큰 저장하는 함수
def save_token_to_file(token):
    with open("config/AuthToken.txt", "w") as file:
        file.write(token)
#토큰 불러오는 함수
def read_token_from_file():
    try:
        with open("config/RefreshToken.txt", "r") as file:
            token = file.read().strip()
            return token
    except FileNotFoundError:
        return None

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