import requests
import config.info as info

client_id = info.id
client_secret = info.secret

# curl -X POST "https://accounts.spotify.com/api/token" \
#      -H "Content-Type: application/x-www-form-urlencoded" \
#      -d "grant_type=client_credentials&client_id=client_id&client_secret=client_secret"

url = "https://accounts.spotify.com/api/token"
header = {"Content-Type": "application/x-www-form-urlencoded"}
data = {"grant_type": "client_credentials", "client_id": client_id, "client_secret": client_secret}

response = requests.post(url,headers=header,data=data)

# 응답 JSON 데이터 디코딩
if response.status_code == 200:  # HTTP OK
    response_json = response.json()
    print("Received JSON response:")
    print(response_json)
else:
    print(f"Error: {response.status_code}")
# JSON 응답에서 원하는 정보 추출 및 사용
if "access_token" in response_json:
    access_token = response_json["access_token"]
    print(f"Value of ‘key’: {access_token}")
else:
    print("Key ‘key’ not found in the JSON response.")