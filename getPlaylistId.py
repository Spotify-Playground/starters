import json

with open("myplaylists.json", "r") as json_file:
    data = json.load(json_file)

# "items" 배열 안의 요소들의 "id" 값을 추출하여 리스트에 저장
ids = [item["id"] for item in data["items"]]

# # 추출된 "id" 값을 출력
# print(ids)
