# git 정리

## git bash

### CLI(Command Line Interface)
    - 명령 기반의 인터페이스
    - 명령어 인터페이스는 사용자와 컴퓨터가 상호 작용하는 방식
    - 인터페이스를 제공하는 프로그램을 명령 줄 해석기 또는 셸이라고 한다.

### GUI(Graphic User Interface)
    그래픽 기반의 인터페이스

### 프롬프트 기본 인터페이스
    - 컴퓨터 정보
    - 디렉토리
    - $

### 명령어 기본 구조
    - 특정 프로그램을 어떠한 인자와 함께 호출하도록 명령

### 디렉토리 관리
    - pwd(print working directory) : 현재 디렉토리 출력
    - cd 디렉토리 이름(change directory) : 디렉토리 이동(. : 현재 디렉토리, .. : 상위 디렉토리)
    - ls(list) : 목록
    - mkdir(make directory) : 디렉토리 생성
    - touch : 파일 생성
    - rm 파일명(remove) : 파일 삭제하기
    - rm -r 폴더명 : 폴더 삭제하기

## git : 분산 버전 관리 시스템
    버전 관리 : 컴퓨터 소프트웨어의 특정 상태

### git 기본 명령어
    1. $ git init : 특정 폴더를 git 저장소를 만들어 git으로 관리
    2. $ git add (file) : working directory상의 변경 내용을 staging area에 추가하기 위해 사용
    3. $ git commit -m '커밋메시지' : staged 상태의 파일들을 커밋을 통해 버전으로 기록
    4. $ git status : 현재 상태 확인
    5. $ git log : 현재 저장소에 기록된 커밋을 조회

### git 기본 흐름
    1. 작업을 하고
    2. 변경된 파일을 모아 (add)
    3. 버전으로 남긴다. (commit)