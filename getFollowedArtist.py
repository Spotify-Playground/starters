import requests
import config.info as info
import json
import module

# curl --request GET \
#   --url 'https://api.spotify.com/v1/me/following?type=artist' \
#   --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'

mytoken = module.read_AuthToken_from_file()

url = "https://api.spotify.com/v1/me/following?type=artist"
header = {
    "Authorization":"Bearer " + mytoken
    }
response = requests.get(url,headers=header)

if response.status_code == 200:  # HTTP OK
    response_json = response.json()
    module.save_FollowedArtist_to_json(response_json)
else:
    print(f"Error: {response.status_code}")