import requests
import os
import json
import module

##playlist별 중복된 track 제거하기

IDS = module.read_playlist_id()
Deduplicated_id = module.deduplicate_tracks(IDS)
AuthToken = module.read_AuthToken_from_file()

# Delete tracks
for playlist in IDS :
    tracks = Deduplicated_id[playlist]
    track_list = list()
    for track in tracks :
        track_uri = {
            "uri" : f"spotify:track:{track}"
        }
        track_list.append(track_uri)
    url = f"https://api.spotify.com/v1/playlists/{playlist}/tracks"
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
    for track in tracks :
        track_uri = f"spotify:track:{track}"
        uris_list.append(track_uri)
    add_data = {
        "uris": uris_list
    }
    
# Add tracks
    add_response = requests.post(url,headers=header,json=add_data)
    add_response_json = add_response.json()

for i in IDS :
    url = f'https://api.spotify.com/v1/playlists/{i}/tracks'
    header = {"Authorization": "Bearer " +AuthToken }
    response = requests.get(url, headers=header)
    response_json = response.json()
    
    directory_path = f"userJS/{i}/"
    os.makedirs(directory_path, exist_ok=True)
    with open(f"userJS/{i}/tracks.json","w")as json_file:
        json.dump(response_json,json_file,indent=4)

    module.insert_track_to_db(i)



