import requests
import json
import module
import Deduplication

def read_Authtoken():
    try:
        with open("config/AuthToken.txt", "r") as file:
            token = file.read().strip()
            return token
    except FileNotFoundError:
        return None

AuthToken = read_Authtoken()

playlist_ids = module.read_playlist_id()
update_ids = Deduplication.dupeled_ids

update_id = module.deduplicate_tracks(playlist_ids)

for pl_id in playlist_ids :
# uris 형태 > uris=spotify:track:4iV5W9uYEdYUVa79Axb7Rh,spotify:track:1301WleyT98MSxVHPZCA6M,spotify:episode:512ojhOuo1ktJprKbVcKyQ
    uris = list()
    for i in update_ids:
        uris.append("spotify:track:"+i)
    Uris = uris.join(",")

    url = f"https://api.spotify.com/v1/playlists/{pl_id}/tracks?uris={Uris}"
    header = {
        "Authorization": "Bearer "+ AuthToken,
        "Content-Type": "application/json"
            }
    data ={
        "range_start": 0,
        "insert_before": 0,
        "range_length": 0
    }

