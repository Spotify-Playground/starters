import requests
import config.info as info
import base64

client_id = info.id
client_secret = info.secret

# curl -X POST "https://accounts.spotify.com/api/token" \
#      -H "Content-Type: application/x-www-form-urlencoded" \
#      -d "grant_type=client_credentials&client_id=client_id&client_secret=client_secret"

url = "https://accounts.spotify.com/api/token"
header = {'Authorization': 'Basic ' + base64.b64encode((client_id + ':' + client_secret).encode()).decode()}
data = {
    "grant_type": "refresh_token",
    "refresh_token": "AQDU3sphRuBidot7B0wWHGL8jjbKZb7iRfWEAcvawFfmApwsOgLc_5fUaaFLnwPLd23cQINxgqr3Pk4zInX5DRV1G0gxnf50RULW8qnPgEEJthJW86StnBsW5zKdpVuC0wA" 
}

response = requests.post(url,headers=header,data=data)

response_json = response.json()
access_token=response_json["access_token"]
print(access_token)