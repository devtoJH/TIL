# 2022.12.28 내용 정리

## 원격저장소 주요 개념
* 원격저장소(Remote Repository) : 원격저장소를 제공하는 서비스는 다양하다.
* git : 버전 관리
* github : 버전 관리

### push($ git push)
* 로컬 저장소의 버전을 원격저장소로 보낸다.

### pull($ git pull)
* 원격저장소의 버전을 로컬저장소로 가져온다.

---

## github 기반 원격 저장소 활용
### 초기 원격저장소 설정하는 법
    1. github 페이지에서 로그인 후, new클릭
    2. 저장소 설정하기
    3. url 확인
    4. 로컬저장소에 원격저장소 정보 설정하기(로컬저장소에는 한 번만 설정하면 됨)
    5. 원격저장소의 정보를 확인

### 로컬저장소의 버전을 원격저장소로 push하기
* 원격저장소로 로컬저장소 변경사항(커밋)을 올림(push)
### push 주의사항
* push할 때는 인증 정보가 필수
* push가 authentication failed되는 경우 인증 정보 확인

### 로컬저장소의 버전을 원격저장소로 pull하기
* $ git pull <원격저장소 이름> <브랜치 이름>

### clone : $ git clone <원격저장소 주소>
* 원격저장소를 복제하여 가져옴

### clone과 pull의 차이점
* clone : 원격저장소 복제
* pull : 원격저장소 커밋 가져오기
* 로컬에서 새로운 프로젝트 시작 : git init
* 원격에 있는 프로젝트 시작 : git clone
* 프로젝트 개발 중 다른 사람 커밋 받아오기 : git pull
* 내가 한 로컬 프로젝트 개발 공유 : git push

## 명령어
* git clone (url) : 원격저장소 복제
* git remote -v : 원격저장소 정보 확인
* git remote add <원격저장소> (url) : 원격저장소 추가(일반적으로 origin)
* git push <원격저장소> <브랜치> : 원격저장소에 push
* git pull <원격저장소> <브랜치> : 원격저장소로부터 pull

## push conflict
    1. 원격저장소의 커밋을 원격저장소로 가져와서(pull)
    2. 로컬에서 두 커밋을 병합(추가 커밋 발생)
    3. 다시 github으로 push

## gitignore
* 일반적인 개발 프로젝트에서 버전 관리를 별도로 하지 않는 파일/디렉토리가 발생
* git 저장소에 .gitignore 파일을 생성하고 해당 내용을 관리
* ***주의 : 이미 커밋된 파일은 반드시 삭제를 하여야 .gitignore로 적용됨***
* 개발 언어 url : https://github.com/github/gitignore
* 개발 환경 : 운영체제(windows, mac, linux), 텍스트 에디터 / IDE(visual studio code 등)