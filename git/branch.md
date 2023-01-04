# Branch : 독립적인 작업흐름을 만들고 관리

## branch 주요 명령어
    1. 브랜치 생성
        (master) $ git branch {branch name}
    2. 브랜치 이동
        (master) $ git checkout {branch name}
    3. 브랜치 생성 및 이동
        (master) $ git checkout -b {branch name}
    4. 브랜치 목록
        (master) $ git branch
    5. 브랜치 삭제
        (master) $ git branch -d {branch name}

## merge
* 각 branch에서 작업을 한 이후 이력을 합치기 위해 merge명령어를 사용
* 병합을 진행할 때, 서로 다른 이력(commit)에서<br>
    * 동일한 파일을 수정한 경우 충돌이 발생
    * 수정한 이후에 직접 커밋 실행
* 다른 파일을 수정한 경우<br>
    * 충돌 없이 자동으로 merge commit이 생성됨

## (1) merge - fast foward
* 기존 master 브랜치에 변경사항이 없어 단순히 앞으로 이동
    1. feature-a branch로 이동 후 commit
    2. master 별도 변경 없음
    3. master branch로 병합

## (2) merge - merge commit
* 기존 master 브랜치에 변경사항이 있어 병합 커밋 발생
    1. feature-a branch로 이동 후 commit
    2. master branch commit
    3. master branch로 병합

## git flow
* git을 활용하여 협업하는 흐름으로 branch를 활용하는 전략을 의미

### git flow 기본 원칙
    1. master branch는 반드시 배포 가능한 상태여야 한다.
    2. feature branch는 각 기능의 의도를 알 수 있도록 작성한다.
    3. commit message는 매우 중요하며, 명학하게 작성한다.
    4. pull request를 통해 협업을 진행한다.
    5. 변경사항을 반영하고 싶다면, master branch에 병합한다.

## github flow models
* github에서 제시하는 방법 2가지<br>
    1. shared repository model
    2. fork & pull model
* 가장 큰 차이점은 내(작업자)가 원격저장소에 직접적인 push권한이 있는지 여부

## shared repository model
* shared repository model은 동일한 저장소를 공유하여 활용하는 방식
* 예시는 작업 흐름을 master + feature 브랜치로 구성하여 진행

## github pull request

### 1. github fork
    1) fork할 저장소에서 우측 상단의 fork버튼을 클릭
    2) 자신의 원격저장소에 저장될 이름을 작성하고 create fork 클릭
    3) 자신의 원격저장소에서 확인한다.

### 2. (local) clone & branch 생성
    1) fork 받아온 저장소를 로컬로 clone 한다.
    >>> clone url 반드시 확인!! 본인의 저장소여야 한다.
    2) branch를 생성하고 이동한다.

### 3. (local) 폴더에 추가하고 커밋
    1) 해당 폴더에 README.md 파일 추가해 작성한다.
    2) 작업 완료 후 변경 사항을 git add, commit, push 한다.

### 4. (github) pull request
    1) github에서 compare & pull request 클릭하거나 좌측 상단의 pull request 클릭
    2) pull request 내용을 작성한 후 create pull request 클릭
        - head repository와 base repository를 확인한다.
        - head => base 방향으로 merge 된다.
        
