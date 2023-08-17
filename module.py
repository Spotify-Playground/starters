import requests
import json
import os
from flask import Flask, redirect, request, jsonify
import random
import string
import base64
import config.info as info
import psycopg2
import config.database_info as db

# login에 필요한 랜덤 16자리 state값 만들기
def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))
# Refresh Token 저장(text파일)
def save_RefreshToken_to_file(token):
    with open("config/RefreshToken.txt", "w") as file:
        file.write(token)

# Access Token 저장(text파일)
def save_AccessToken_to_file(token):
    with open("config/AuthToken.txt", "w") as file:
        file.write(token)
        
# AuthToken 불러오기
def read_AuthToken_from_file():
    try:
        with open("config/AuthToken.txt", "r") as file:
            token = file.read().strip()
            return token
    except FileNotFoundError:
        return None
    
# RefreshToken 불러오기
def read_RefreshToken_from_file():
    try:
        with open("config/RefreshToken.txt", "r") as file:
            token = file.read().strip()
            return token
    except FileNotFoundError:
        return None

# 내 playlist정보 저장하기(json파일)
def save_MyPlaylist_to_json(response_json):
    with open("userJS/myplaylists.json", "w") as json_file:
        json.dump(response_json, json_file, indent=4)
        
# follow 한 artist 정보 저장하기(json파일)
def save_FollowedArtist_to_json(response_json):
    with open("userJS/followed_artist.json", "w") as json_file:
        json.dump(response_json, json_file, indent=4)

# 내 playlist 의 ID 값가져오기
def read_playlist_id():
    with open("userJS/myplaylists.json", "r") as json_file:
        data = json.load(json_file)
    # "items" 배열 안의 요소들의 "id" 값을 추출하여 리스트에 저장
    ids = [item["id"] for item in data["items"]]
    return ids

# playlist의 중복track 제거 
def deduplicate_alltracks(ids):
    deduplicated_ids = set()
    for playlist_id in ids:
        with open(f"userJS/{playlist_id}/tracks.json", "r") as json_file:
            data = json.load(json_file)
            # "items" 배열 안의 요소들의 "id" 값을 추출하여 리스트에 저장
            for item in data["items"]:
                if "track" in item and "id" in item["track"]:
                    deduplicated_ids.add(item["track"]["id"])
    # 중복제거된 track_list 반환
    return list(deduplicated_ids)
# playlist의 중복track 제거 
def deduplicate_tracks(ids):
    deduplicated_tracks = {}  # 플레이리스트 ID를 키로, 중복 제거된 트랙 ID 리스트를 값으로 저장
    for playlist_id in ids:
        deduplicated_ids = set()
        with open(f"userJS/{playlist_id}/tracks.json", "r") as json_file:
            data = json.load(json_file)
            # "items" 배열 안의 요소들의 "id" 값을 추출하여 집합에 저장
            for item in data["items"]:
                if "track" in item and "id" in item["track"]:
                    deduplicated_ids.add(item["track"]["id"])
        deduplicated_tracks[playlist_id] = list(deduplicated_ids)
    return deduplicated_tracks

# db에 json 저장
def insert_track_to_db(id):
    # 커넥터
    conn = psycopg2.connect(
        database = db.database,
        user = db.user,
        password = db.password,
        host = db.host,
        port = db.port
    )
    # 커서
    cur = conn.cursor()
    # JSON 데이터를 문자열로 변환하여 저장
    with open(f"userJS/{id}/tracks.json", "r") as json_file:
        json_data = json.load(json_file)
    type = "track"
    json_string = json.dumps(json_data)
    query = "INSERT INTO test1 (content,type) VALUES (%s, %s)"
    cur.execute(query, (json_string,type))

    # 커밋 및 연결 닫기
    conn.commit()
    cur.close()
    conn.close()
    
def insert_playlist_to_db():
    # 커넥터
    conn = psycopg2.connect(
        database = db.database,
        user = db.user,
        password = db.password,
        host = db.host,
        port = db.port
    )
    # 커서
    cur = conn.cursor()
    # JSON 데이터를 문자열로 변환하여 저장
    with open(f"userJS/myplaylists.json", "r") as json_file:
        json_data = json.load(json_file)
    type = "playlist"
    json_string = json.dumps(json_data)
    query = "INSERT INTO test1 (content,type) VALUES (%s, %s)"
    cur.execute(query, (json_string,type))

    # 커밋 및 연결 닫기
    conn.commit()
    cur.close()
    conn.close()