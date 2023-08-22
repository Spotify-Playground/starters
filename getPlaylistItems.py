import requests
import json
import os
import module

IDS = module.read_playlist_id()
AuthToken = module.read_AuthToken_from_file()
# curl 예시
# curl --request GET \
#   --url https://api.spotify.com/v1/playlists/3cEYpjA9oz9GiPac4AsH4n/tracks \
#   --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'

for i in IDS :
    url = f'https://api.spotify.com/v1/playlists/{i}/tracks'
    header = {"Authorization": "Bearer " +AuthToken }
    response = requests.get(url, headers=header)
    response_json = response.json()
    
    directory_path = f"userJS/{i}/"
    os.makedirs(directory_path, exist_ok=True)
    with open(f"userJS/{i}/tracks.json","w")as json_file:
        json.dump(response_json,json_file,indent=4)