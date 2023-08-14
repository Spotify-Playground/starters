import json
import os

playlists_dirs = [dir for dir in os.listdir("db") if not dir.endswith(".json")]
for dir in playlists_dirs :
    with open(f"db/{dir}/tracks.json", "r") as file:
        tracks_json = json.load(file)
        tracks_item = tracks_json["items"]
        tracks_ids = set()
        for item in tracks_item :
            tracks_ids.add(item["track"]["id"])
        with open(f"db/{dir}/tracks_id.txt", "w") as file :
            for id in tracks_ids :
                file.write(id+"\n")