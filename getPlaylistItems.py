import requests
import getPlaylistId
import json
import os

IDS = getPlaylistId.ids

# curl --request GET \
#   --url https://api.spotify.com/v1/playlists/3cEYpjA9oz9GiPac4AsH4n/tracks \
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

for i in IDS :
    url = f'https://api.spotify.com/v1/playlists/{i}/tracks'
    header = {"Authorization": "Bearer " +AuthToken }
    response = requests.get(url, headers=header)
    response_json = response.json()
    
    directory_path = f"userJS/{i}/"
    os.makedirs(directory_path, exist_ok=True)
    with open(f"userJS/{i}/tracks.json","w")as json_file:
        json.dump(response_json,json_file,indent=4)
    
    