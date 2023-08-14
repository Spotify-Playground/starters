from flask import Flask, redirect, request, jsonify
import random
import string
import requests
import base64
import json

app = Flask(__name__)

def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def save_RefreshToken_to_file(token):
    with open("configs/RefreshToken.txt", "w") as file:
        file.write(token)

def save_AccessToken_to_file(token):
    with open("configs/AuthToken.txt", "w") as file:
        file.write(token)
        
def get_credential(key) :
    try: 
        with open("configs/credential.json", "r") as file :
            credential = json.load(file)
            return credential[key]
    except FileNotFoundError:
        return None

client_id = get_credential("ID")
client_secret = get_credential("SECRETS")
redirect_uri = get_credential("RED_URI")
state_key = 'spotify_auth_state'

@app.route('/login')
def login():
    state = generate_random_string(16)
    response = redirect('https://accounts.spotify.com/authorize?' + 
                        f'response_type=code&client_id={client_id}&' +
                        f'scope=user-read-private%20user-read-email&' +
                        f'redirect_uri={redirect_uri}&state={state}')
    response.set_cookie(state_key, state)    
    return response

@app.route('/callback')
def callback():
    code = request.args.get('code', None)
    state = request.args.get('state', None)
    stored_state = request.cookies.get(state_key)
    
    # if state is None or state != stored_state:
    #     return 'Invalid state parameter', 400

    response = requests.post('https://accounts.spotify.com/api/token', data={
        'code': code,
        'redirect_uri': redirect_uri,
        'grant_type': 'authorization_code',
    }, headers={
        'Authorization': 'Basic ' + base64.b64encode((client_id + ':' + client_secret).encode()).decode()
    })

    if response.status_code == 200:
        data = response.json()
        access_token = data['access_token']
        refresh_token = data.get('refresh_token', None)
        save_AccessToken_to_file(access_token)
        save_RefreshToken_to_file(refresh_token)
        
        user_response = requests.get('https://api.spotify.com/v1/me', headers={
            'Authorization': 'Bearer ' + access_token
        })

        user_data = user_response.json()
        return jsonify({'user_data': user_data, 'access_token': access_token, 'refresh_token': refresh_token})
    return 'Error during token exchange', 400
if __name__ == '__main__':
    app.run(port=3000)
