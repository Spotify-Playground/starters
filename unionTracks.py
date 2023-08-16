import os
import requests
import json

playlists_dirs = [dir for dir in os.listdir("db") if not dir.endswith(".json")]

all_tracks = set()
for dir in playlists_dirs :
    with open(f"db/{dir}/tracks_id.txt", "r") as file:
        for f in file.readlines() :
            all_tracks.add(f.strip())

def get_credential(key) :
    try: 
        with open("configs/credential.json", "r") as file :
            credential = json.load(file)
            return credential[key]
    except FileNotFoundError:
        return None

user_id = get_credential("USER_ID")

def read_AccessToken_to_file():
    with open("configs/AuthToken.txt", "r") as file:
        token = file.read()
        return token

access_token = read_AccessToken_to_file()

url = f"https://api.spotify.com/v1/users/{user_id}/playlists"
header = {
    'Authorization': 'Bearer ' +access_token,
    'Content-Type': 'application/json'
}
data = {
    "name": "Total Playlist",
    "description": "Total",
    "public": False
}

response = requests.post(url,headers=header,json=data)
response_json = response.json()
total_playlist_id = response_json["id"]


url = f"https://api.spotify.com/v1/playlists/{total_playlist_id}/tracks"
data = {
    "uris": [ 
        "spotify:track:4iV5W9uYEdYUVa79Axb7Rh", 
        "spotify:track:1301WleyT98MSxVHPZCA6M", 
        "spotify:episode:512ojhOuo1ktJprKbVcKyQ"
    ]
}
# curl --request POST \
#   --url https://api.spotify.com/v1/playlists/054pYYA6qQ2qttFz6MrmIl/tracks \
#   --header 'Authorization: Bearer BQB9JSvp0i-VohoeadsakgWpF5awz8199nSYEcp6XNYJdnR47FIWDuI3mkWFTN3mcK8FTr4RHOoChBv8rE_Z83M64QBHOgzozsB3IXjGZxYaU_dP-KtFkKZ0EqB8g9ePuMJaMydYx29SLrtQQg1zMSELLQv3wRF7XWIVTSbOtFZpaMfXhBsqIaf879U0c6nwkE-uo_VDTcW9mJU6couscl_yHz_67duspTtXbGuzVc9aEI9Vt2mMUUXfwdsc6S14EKmCAF2loMsvmPsmOcKbK_A6fDxLhtk8Mp7X' \
#   --header 'Content-Type: application/json' \
#   --data '{
#     "uris": ["spotify:track:4iV5W9uYEdYUVa79Axb7Rh","spotify:track:1301WleyT98MSxVHPZCA6M"
#     ],
#     "position": 0
# }'

response = requests.post(url,headers=header,json=data)
response_json = response.json()
print(response_json)