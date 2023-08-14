import requests
import config.info as info

# curl --request GET \
#   --url 'https://api.spotify.com/v1/me/following?type=artist' \
#   --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
# authoToken 불러오는 함수
def read_Authtoken():
    try:
        with open("config/AuthToken.txt", "r") as file:
            token = file.read().strip()
            return token
    except FileNotFoundError:
        return None


mytoken = read_Authtoken()
print(mytoken)
url = "https://api.spotify.com/v1/me/following?type=artist"
header = {"Authorization":"Bearer " + mytoken}
# header = f" --header 'Authorization: Bearer {mytoken}'"
response = requests.get(url,headers=header)

if response.status_code == 200:  # HTTP OK
    response_json = response.json()
    print("Received JSON response:")
    print(response_json)
else:
    print(f"Error: {response.status_code}")