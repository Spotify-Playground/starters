# starters

Spotify 사용자 데이터 기반 개인화 서비스 

## Functions (TBU)
- 스포티파이 재생목록을 개인의 재생 기록을 기반으로 필터링 구성
- N회 재생한 곡은 재생목록에 없으면 추가
- 최근 듣지 않은 곡은 재생목록에서 삭제
- 재생목록 내 중복된 노래 제거
- 자주 재생한 아티스트/장르의 곡 중 인기
- 팔로우 아티스트의 신곡 알림
- 

## Data
- Spotify Web API

## Architectures

### 데이터 수집 및 적재
- Spotify Web API 에 Curl 요청해 응답받은 Json, GCP 스토리지 적재

### 데이터 전처리 
- GCP 스토리지에 적재된 Json을 Python 또는 SQL 로 전처리 후 PostgreSql 디비에 적재

### 서버 사용 및 배포
- GCP 엔진 3개 및 스토리지 사용

# Stacks
- Python
- Airflow
- PostgreSql
- Fast API
- Google Cloud Platform
- Docker
