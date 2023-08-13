import requests
import config.client as client

CLIENT_ID = client.ID
CLIENT_SECRETS = client.SECRETS

# API 엔드포인트 URL
# url = "https://example.com/api_endpoint"
url = "https://accounts.spotify.com/api/token"
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}
data = {
    "grant_type": "client_credentials",
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRETS
}

# 요청 보내고 응답 받기
# response = requests.get(url)
response = requests.post(url, headers=headers, data=data)

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
    print(f"Value of 'key': {access_token}")
else:
    print("Key 'key' not found in the JSON response.")