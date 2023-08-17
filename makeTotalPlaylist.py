import module
import config.info as info
import requests
import os
import json

user_id = info.user_id
AuthToken = module.read_AuthToken_from_file()
ids = module.read_playlist_id()
all_tracks = module.deduplicate_alltracks(ids)
print(len(all_tracks))

url = f"https://api.spotify.com/v1/users/{user_id}/playlists"
header = {
    'Authorization': 'Bearer ' +AuthToken,
    'Content-Type': 'application/json'
}
data = {
    "name": "Total Playlist",
    "description": "Total",
    "public": False
}

total_dir = [dir for dir in os.listdir("userJS") if dir.startswith("total")]
if (not total_dir) :
    response = requests.post(url,headers=header,json=data)
    print(total_dir)

    if response.status_code == 201:
        response_json = response.json()
        total_playlist_id = response_json["id"]
        with open("config/total_playlist_id.txt","w") as file:
            file.write(f"{total_playlist_id}")

        os.makedirs(f"userJS/total_{total_playlist_id}",exist_ok=True)

        uri_prefix = "spotify:track:"
        uris = list()
        for track in all_tracks :
            uris.append(uri_prefix+track)
        
        url = f"https://api.spotify.com/v1/playlists/{total_playlist_id}/tracks"
        data = {
            "uris": uris
        }

        response = requests.post(url,headers=header,json=data)
        
        
        url = f'https://api.spotify.com/v1/playlists/{total_playlist_id}/tracks'
        header = {"Authorization": "Bearer " +AuthToken }
        response = requests.get(url, headers=header)
        response_json = response.json()
        
        with open(f"userJS/total_{total_playlist_id}/tracks.json","w") as json_file:
            json.dump(response_json,json_file,indent=4)

else :
    track_list=list()
    for track in all_tracks :
        track_uri = {
            "uri" : f"spotify:track:{track}"
        }
        track_list.append(track_uri)
    total_playlist_id = total_dir.pop().replace("total_","")
    url = f"https://api.spotify.com/v1/playlists/{total_playlist_id}/tracks"
    header = {
        "Authorization": "Bearer " + AuthToken,
        "Content-Type": "application/json"
    }
    del_data = {
        "tracks" : track_list
    }
    del_response = requests.delete(url, headers=header, json=del_data)
    del_response_json = del_response.json()
    
    uris_list = list()
    for track in all_tracks :
        track_uri = f"spotify:track:{track}"
        uris_list.append(track_uri)
    add_data = {
        "uris": uris_list
    }
    add_response = requests.post(url,headers=header,json=add_data)
    add_response_json = add_response.json()

    url = f"https://api.spotify.com/v1/playlists/{total_playlist_id}/tracks"
    header = {
        'Authorization': 'Bearer ' + AuthToken
    }
    response = requests.get(url,headers=header)
    response_json = response.json()
    
    with open(f"userJS/total_{total_playlist_id}/tracks.json","w") as json_file:
        json.dump(response_json,json_file,indent=4)