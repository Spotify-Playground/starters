import requests
import os
import json
import getPlaylistId

#playlist_id의 리스트
# IDS = getPlaylistId.ids

# print(IDS[0])

dupeled_ids = set()

with open(f"userJS/5Eep9aW50tB4gbdEDpw2N3/tracks.json", "r") as json_file:
    data = json.load(json_file)

# # "items" 배열 안의 요소들의 "id" 값을 추출하여 리스트에 저장
# dupeled_ids = [item["id"] for item in data["items"]]

# print(dupeled_ids)
for item in data["items"]:
    if "track" in item and "id" in item["track"]:
        dupeled_ids.add(item["track"]["id"])

dupeled_ids = list(dupeled_ids)
print(dupeled_ids)


