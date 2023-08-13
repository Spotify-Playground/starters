import requests
import config.info as info
import getTokenbyCredential

# curl --request GET \
#   --url 'https://api.spotify.com/v1/me/following?type=artist' \
#   --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'

mytoken = getTokenbyCredential.read_token_from_file()

url = "https://api.spotify.com/v1/me/following?type=artist"
header = {
    "Authorization": "Bearer "+mytoken
}

response = requests.get(url, headers=header)

if response.status_code == 200:  # HTTP OK
    response_json = response.json()
    print("Received JSON response:")
    print(response_json)
else:
    print(f"Error: {response.status_code}")