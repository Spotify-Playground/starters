import json
import os
import requests

def read_AccessToken_to_file():
    with open("configs/AuthToken.txt", "r") as file:
        token = file.read()
        return token

access_token = read_AccessToken_to_file()

with open("db/usersplaylists.json", "r") as file :
    usersplaylists_json = json.load(file)
    usersplaylists_items = usersplaylists_json["items"]
    for item in usersplaylists_items :
        os.makedirs(f"db/playlist_{item['id']}",exist_ok=True)
        url = f"https://api.spotify.com/v1/playlists/{item['id']}/tracks"
        header = {
            'Authorization': 'Bearer ' + access_token
        }
        response = requests.get(url,headers=header)
        response_json = response.json()

        with open(f"db/playlist_{item['id']}/tracks.json", "w") as file :
            json.dump(response_json,file,indent=4)