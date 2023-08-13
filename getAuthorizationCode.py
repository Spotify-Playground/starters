import requests
import random
import string
from flask import Flask, request, redirect, make_response
import urllib.parse

client_id = 'ec7c9f15df104a378127fe610dbeb080'
client_secret = 'bb44c6e4b6ff41b0bfba88c4985d815f'
redirect_uri = 'http://localhost:8888/callback'
state_key = 'spotify_auth_state'

app = Flask(__name__)

def generate_random_string(length):
    possible = string.ascii_letters + string.digits
    return ''.join(random.choice(possible) for _ in range(length))

@app.route('/login')
def login():
    state = generate_random_string(16)
    response = make_response(redirect_uri)
    response.set_cookie(state_key, state)
    
    scope = 'user-read-private user-read-email'
    params = {
        'response_type': 'code',
        'client_id': client_id,
        'scope': scope,
        'redirect_uri': redirect_uri,
        'state': state
    }
    redirect_url = 'https://accounts.spotify.com/authorize?' + urllib.parse.urlencode(params)
    
    return redirect(redirect_url)

@app.route('/callback')
def callback():
    code = request.args.get('code')
    state = request.args.get('state')
    stored_state = request.cookies.get(state_key)
    
    if state is None or state != stored_state:
        return 'State mismatch'
    else:
        response = make_response(redirect_uri)
        response.delete_cookie(state_key)
        
        auth_options = {
            'url': 'https://accounts.spotify.com/api/token',
            'data': {
                'code': code,
                'redirect_uri': redirect_uri,
                'grant_type': 'authorization_code'
            },
            'headers': {
                'Authorization': 'Basic ' + (client_id + ':' + client_secret).encode('utf-8').b64encode().decode('utf-8')
            }
        }
        
        response = requests.post(auth_options['url'], data=auth_options['data'], headers=auth_options['headers'])
        if response.status_code == 200:
            data = response.json()
            access_token = data.get('access_token')
            refresh_token = data.get('refresh_token')
            
            options = {
                'url': 'https://api.spotify.com/v1/me',
                'headers': {
                    'Authorization': 'Bearer ' + access_token
                }
            }
            
            response = requests.get(options['url'], headers=options['headers'])
            if response.status_code == 200:
                user_data = response.json()
                print(user_data)
            
            return 'Access token: ' + access_token + '\nRefresh token: ' + refresh_token
        else:
            return 'Invalid token'

if __name__ == '__main__':
    app.run(port=8888)
