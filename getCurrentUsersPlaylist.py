import requests
import json

# curl --request GET \
#   --url https://api.spotify.com/v1/me/playlists \
#   --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'

# authoToken 불러오는 함수
def read_Authtoken():
    try:
        with open("config/AuthToken.txt", "r") as file:
            token = file.read().strip()
            return token
    except FileNotFoundError:
        return None

AuthToken = read_Authtoken()
url = "https://api.spotify.com/v1/me/playlists"
header = {'Authorization':'Bearer ' + AuthToken}

response = requests.get(url, headers=header)

if response.status_code == 200:  # HTTP OK
    response_json = response.json()
    print("Received JSON response:")
    print(response_json)
    with open("myplaylists.json", "w") as json_file:
        json.dump(response_json, json_file, indent=4)  # JSON 파일에 저장 (들여쓰기 포함)
else:
    print(f"Error: {response.status_code}")