![image](https://github.com/Spotify-Playground/starters/assets/131243101/47fec427-2095-4217-aa0c-14876d03f2c6)

## [OwlsClub] Spotify API 서비스 개발
Spotify 어플리케이션(모바일/데스크톱/웹)과 상호작용하는 API 서비스 개발 <br>

> **Spotify 사용자 데이터 기반 개인화 서비스** <br>
Spotify 스트리밍 서비스 사용자의 로그를 기반으로 Spotify 컨텐츠를 개인 맞춤으로 제공하는 서비스 <br>

→ Spotify 스트리밍 서비스 사용이 낯설고 Spotify 제공 컨텐츠에 대한 제약으로, 추천 알고리즘에 필요한 데이터 수집 및 가공 어려움 <br>
→ 실력과 시간의 한계로 방향 수정, 기능 축소 <br>

### API Services

- Access Authorization 
  - 1시간 단위로 만료되는 토큰 갱신 발급 (이후 1시간 단위)
  - 토큰 갱신에 사용되는 토큰 발급 (서버 실행시 초기 1회만)
- User's Playlists & Tracks
  - 사용자의 재생목록과 재생목록별 트랙 정보 업데이트
  - 재생목록에서 중복되는 트랙 제거
- Unified Track Playlist
  - 사용자 트랙의 통합 재생목록 구성 & 업데이트

<img width="329" alt="spotify 앱 플레이리스트" src="https://github.com/Spotify-Playground/starters/assets/131243101/8b6a8575-7bd6-4569-9328-114e1695ba75"> <br>
<img width="311" alt="유저 플레이리스트 폴더" src="https://github.com/Spotify-Playground/starters/assets/131243101/b00dcae5-4fa0-4f1c-ab23-07c36dd7066b">



## Data 
[Spotify Web API](https://developer.spotify.com/documentation/web-api) 

- **사용한 API Calls**
  <br> [Get Current User's Playlists](https://developer.spotify.com/documentation/web-api/reference/get-a-list-of-current-users-playlists)
  <br> [Get User's Playlists](https://developer.spotify.com/documentation/web-api/reference/get-list-users-playlists)
  <br> [Get Playlist Items](https://developer.spotify.com/documentation/web-api/reference/get-playlists-tracks)
  <br> [Create Playlist](https://developer.spotify.com/documentation/web-api/reference/create-playlist)
  <br> [Remove Playlist Items](https://developer.spotify.com/documentation/web-api/reference/remove-tracks-playlist)
  <br> [Add Items to Playlist](https://developer.spotify.com/documentation/web-api/reference/add-tracks-to-playlist)
  <br> [Update Playlist Items](https://developer.spotify.com/documentation/web-api/reference/reorder-or-replace-playlists-tracks)

- **Json**
  <br> UserData
  <br> Playlist
  <br> Tracks
  <br> <img width="885" alt="playlist_track1" src="https://github.com/Spotify-Playground/starters/assets/131243101/987e9a76-270b-4bd8-a573-a0e0b24211a2">


## Architecture

- **개발환경: Pyenv+Pipenv으로 환경세팅** <br>
  <img width="355" alt="pipfile 캡처" src="https://github.com/Spotify-Playground/starters/assets/131243101/64a2cef0-742d-4fd2-9b9c-16cd9836ec5c"> <br><br>
  
- **데이터 [수집 ~ 가공 ~ 적재] 모두 파이썬 스크립트로 구현** <br>
  <img width="307" alt="py 모음" src="https://github.com/Spotify-Playground/starters/assets/131243101/ed37a244-bfbf-42ee-a222-1f4ede2c9bf6"> <br>
  <img width="1039" alt="authorization 캡처" src="https://github.com/Spotify-Playground/starters/assets/131243101/67a54f21-8642-41a7-9ef4-25886ffdd840"> <br>
  <img width="874" alt="refreshtoken 캡처" src="https://github.com/Spotify-Playground/starters/assets/131243101/2e0fcb40-6db8-4db9-aaf6-abbd5342058f"> <br>
  <img width="630" alt="getplaylistid 캡처" src="https://github.com/Spotify-Playground/starters/assets/131243101/1ad97009-aa51-42b9-89b5-7e5412717654"> <br>
  <img width="708" alt="getplaylistitems 캡처" src="https://github.com/Spotify-Playground/starters/assets/131243101/1a864a37-c45a-44e5-a270-61c1b6822627"> <br>
  <img width="633" alt="deduplication 캡처" src="https://github.com/Spotify-Playground/starters/assets/131243101/8e062fde-804c-470a-a557-0bff73620de7"> <br><br>
  
- **로컬에 설치한 PostgreSql 에 Json 적재**
  <img width="779" alt="db 캡처" src="https://github.com/Spotify-Playground/starters/assets/131243101/35d9caf4-16cf-413c-8b3e-0331254b506d">
  <img width="550" alt="dbtest 캡처" src="https://github.com/Spotify-Playground/starters/assets/131243101/785c64e7-28e0-481d-b0d1-b21b03bd112e"> <br><br>

## Stacks

<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/spotify-1DB954?style=for-the-badge&logo=spotify&logoColor=white"> <img src="https://img.shields.io/badge/flask-000000?style=for-the-badge&logo=flask&logoColor=white"> <img src="https://img.shields.io/badge/postgresql-4169E1?style=for-the-badge&logo=postgresql&logoColor=white"> <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white">
