import requests
import json
import os
from flask import Flask, redirect, request, jsonify
import random
import string
import base64
import config.info as info

app = Flask(__name__)

client_id = info.id
client_secret = info.secret
redirect_uri = info.RED_URI
state_key = 'spotify_auth_state'

def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def save_RefreshToken_to_file(token):
    with open("config/RefreshToken.txt", "w") as file:
        file.write(token)

def save_AccessToken_to_file(token):
    with open("config/AuthToken.txt", "w") as file:
        file.write(token)
#토큰 불러오는 함수
def read_AuthToken_from_file():
    try:
        with open("config/AuthToken.txt", "r") as file:
            token = file.read().strip()
            return token
    except FileNotFoundError:
        return None


#getTokenbyAuthorizationCode.py
#def get
