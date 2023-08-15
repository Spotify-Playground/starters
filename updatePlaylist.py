import requests
import json
import Deduplication

def read_Authtoken():
    try:
        with open("config/AuthToken.txt", "r") as file:
            token = file.read().strip()
            return token
    except FileNotFoundError:
        return None

AuthToken = read_Authtoken()

update_ids = Deduplication.dupeled_ids

# ['5nCwjUUsmBuNZKn9Xu10Os', '5xrtzzzikpG3BLbo4q1Yul', '0pYacDCZuRhcrwGUA5nTBe']
# uris=spotify:track:4iV5W9uYEdYUVa79Axb7Rh,spotify:track:1301WleyT98MSxVHPZCA6M,spotify:episode:512ojhOuo1ktJprKbVcKyQ
uris = list()
for i in update_ids:
    uris.append("spotify:track:"+i)
Uris = uris.join(",")

url = f"https://api.spotify.com/v1/playlists/5Eep9aW50tB4gbdEDpw2N3/tracks?uris={Uris}"
header = {
    "Authorization": "Bearer "+ AuthToken,
    "Content-Type": "application/json"
          }
data ={
    "range_start": 0,
    "insert_before": 0,
    "range_length": 0
}

