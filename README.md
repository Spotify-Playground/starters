## starters : OwlsClub 
![image](https://github.com/Spotify-Playground/starters/assets/131243101/47fec427-2095-4217-aa0c-14876d03f2c6)

### Spotify 사용자 데이터 기반 개인화 서비스

세계 최대의 음원 스트리밍 서비스 Spotify <br>
사용자 데이터를 통해 개인 맞춤형 컨텐츠를 제공해 <br>
사용자의 사용 경험을 더 올릴 수 있을 .. 것으로 기대 <br>
데이터 활용 계획 (정석님 포부 유튜브 플리 업로드)

### Functions (Planned)
- 재생목록에서 중복된 노래 제거
- 사용자 통합 재생목록 생성
- 사용자 통합 재생목록 갱신
- 사용자 선호 장르 별 트랙 추천

### Functions (Backlog)
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
- Fast API
- PostgreSql
- Google Cloud Platform
- Docker
