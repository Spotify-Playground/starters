import psycopg2
import config.database_info as db
import json
import module
# 커넥터
conn = psycopg2.connect(
    database = db.database,
    user = db.user,
    password = db.password,
    host = db.host,
    port = db.port
)
ids = module.read_playlist_id()
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