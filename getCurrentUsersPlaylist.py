import requests
import json
import os
import module

# curl --request GET \
#   --url https://api.spotify.com/v1/me/playlists \
#   --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'

AuthToken = module.read_AuthToken_from_file()

url = "https://api.spotify.com/v1/me/playlists"
header = {
    'Authorization':'Bearer ' + AuthToken
    }
response = requests.get(url, headers=header)

if response.status_code == 200:  # HTTP OK
    response_json = response.json()
    module.save_MyPlaylist_to_json(response_json)
else:
    print(f"Error: {response.status_code}")