# Using Version Management

## Upload an App to a Version-Controlled Repository

- Mendix에서 새 앱을 시작하면 시스템이 자동으로 앱용 저장소 생성을 제안함
- 아직 버전 관리 대상이 아닌 앱은 나중에 버전 관리 저장소에 연결할 수 있음
- 이는 다른 앱을 재사용하거나 기존 앱의 복사본을 만들 때 발생할 수 있음
- 이 경우 Mendix는 버전 관리 아래에 있는 버전 관리 서버에 업로드 옵션을 제공함
    
    → 상단 메뉴바에서 Version Control 탭에서 Upload to Version Control Server 클릭
    

## History

- 앱 기록을 통해 지금까지 앱에 적용된 변경 사항을 볼 수 있음
- 이러한 변경 사항에 따라 새로 추가된 기능 중 일부를 실행 취소해야 하는 경우 앱을 되돌리려는 지점을 선택할 수 있음
- 개발자 포털 또는 Studio Pro 내에서 기록을 볼 수 있음

- Mendix 개발자 포털의 앱 페이지에서 Collaborate > Team Server로 이동하면 다음 4가지 유형의 이벤트가 있음
    - Commits
    - Created tags
    - Created branch lines
    - Deleted branch lines

*참고 : 태그된 버전은 Mendix 배포 패키지를 빌드하는 데 사용된 개정판이다*

- 한 줄에 다음이 표시됨
    - The avatar of the actor
    - A message
    - The date and time of the event
    - The name of the actor who has triggered the event
    - On which line of the app the event was triggered
    - The used Mendix Studio Pro version (For tag events, we do not show the Mendix Studio Pro version)
    - The revision number after the event
    - The related user stories

- Mendix Studio Pro 내에서 Version Control > History…로 이동하면 다음 2가지 유형의 이벤트를 볼 수 있음
    - The revision number
    - A symbol, indicating the type of change

## ****Including Snapshots****

- Mendix에는 로컬 배포에 사용할 수 있는 자체 기본 데이터베이스가 있음
- 이런 벙식으로 외부 데이터베이스에 의존하지 않고 이 내장 데이터베이스를 사용할 수 있음
- 알아두면 좋은 점은 팀과 데이터베이스를 공유할 수 있으므로 팀이 데이터 세트를 사용하여 앱을 테스트할 수도 있다는 것
- 이렇게 하면 시간이 절약되고 발생한 문제를 재현하는 데 도움이 됨
- Mendix Studio Pro를 통해 데이터 스냅샷을 생성하려면 버전 제어 메뉴로 이동하기
    - Version control > Add a snapshot of your data
- 그러면 데이터의 스냅샷이 생성되고 앱의 배포 디렉토리에 zip 파일(data-snapshot.zip)이 추가됨
- 다음에 커밋할 때 지정된 배포 폴더에 압축을 풀어 전체 팀이 이 데이터베이스를 사용할 수 있음

## Conflicts and How to Resolve Them

- 앱에서 함께 작업할 때 팀 서버에 새로운 변경 사항을 커밋하기 전에 해결해야 하는 다양한 유형의 충돌이 나타날 수 있음
- 이러한 충돌은 모델(문서 충돌) 또는 저장소의 일부인 다른 문서(앱 충돌)와 관련될 수 있음
- 애플리케이션 모델 내에서 마지막 업데이트 이후 로컬 작업 복사본에 대한 변경 사항을 나열하는 변경 사항 문서를 열 수 있음
- 로컬 작업 복사본을 온라인 버전으로 업데이트하면 팀 구성원이 변경한 내용이 로컬 버전으로 다운로드 됨
- 팀 구성원이 동일한 문서(예: 페이지 또는 마이크로플로우)에서 작업하는 경우 Studio Pro는 다운로드한 문서 버전과 로컬에 저장된 문서 버전 간에 불일치가 있음을 나타내는 충돌을 식별함

- Mendix Studio Pro는 충돌 없이 변경 사항 커밋을 시행하므로 커밋하기 전에 이 충돌을 해결해야함
    - 먼저 새로 업데이트된 앱 버전과 로컬 앱 버전 간의 차이점을 확인할 것
    - 충돌하는 문서를 변경한 팀원과 연결하여 어떤 버전의 진실을 사용해야 할지 함께 결정할 것
    - 충돌하는 문서(예: 마이크로플로우)의 두 버전을 모두 보려면 Mendix Studio Pro에서 자신만의 마이크로플로우 사본을 생성하고 ‘해당 항목을 사용하여 해결(‘Resolve using theirs)’을 선택하면 됨

- 충돌을 방지하는 방법
    - 먼저 어떤 유형의 변경 사항이 이러한 충돌을 일으킬 수 있는지 확인
    - 충돌에는 수정 - 수정(modify – modify), 수정 - 삭제(modify – delete) 두 가지의 주요 유형이 있음
    
    1. 수정 - 수정(modify – modify)
        1. 귀하와 귀하의 팀 구성원이 정확히 동일한 문서를 수정한 경우 발생
            1. 예를 들어 페이지에 있는 입력 필드의 동일한 레이블 이름 바꾸기
            2. 페이지에 대한 모듈 역할 액세스 설정
            3. 마이크로플로우의 활동 변경
            4. 도메인 모델의 모듈 역할에 대한 엔터티 액세스 규칙 변경 등
    
    1. 수정 - 삭제(modify – delete)
        1. 누군가가 제거한 요소를 변경할 때 발생
            1. 예를 들어 DataGrid에서 열 이름 변경/삭제
            2. 다른 사람이 이 마이크로플로를 삭제한 동안 마이크로플로 변경
            3. 다른 사람이 삭제한 연결 이름 바꾸기 등

1. 이 두 가지 유형 이외에 
    1. 동일한 이름의 문서(페이지, 마이크로플로우 및 기타 문서)를 추가
    2. 동일한 AppStore 모듈을 가져올 때 충돌이 발생

- 충돌을 예방하는 방법
    - 팀원들과 합의
        - 예를 들어 정기적인 업데이트 및 커밋을 수행
        - 작업을 분리
        - 모든 스프린트에서 도메인 모델 기반을 마련

## Opening Older Revisions

- Mendix Studio Pro는 모든 앱 개정을 추적하고 자동으로 저장함
- 이를 통해 필요한 경우 이전 버전의 앱을 열 수 있음
    
    → 이전 버전을 열려면 해당 버전에서 branch를 만들어야 함
    
- 모델의 두 개정판 간의 차이점을 식별하기 위해 또는 실제 환경에 게시된 개정판을 디버깅하기 위해 이전 버전을 열고 싶을 수도 있음
- 그런 다음 새로운 Mendix Studio Pro 세션에서 해당 분기를 열 수 있음
- 이 branch를 보기 및 분석 목적으로만 사용하고 해당 개정 이후에 이미 많은 커밋이 완료되었으므로 이 branch를 변경하지 말 것
- 앱에서 개정판을 추출하는 또 다른 방법도 있지만 이를 위해서는 [TortoiseSVN](https://tortoisesvn.net/support.html)을 사용해야 함

## Using Branches

- 앱이 프로덕션에 게시되면 분기를 만드는 방법을 아는 게 중요
    - 이를 통해 실행 중인 앱에 영향을 주지 않고 기능 개발을 계속 할 수 있음
    - 또한, 새로운 기능 개발과 핫픽스를 분리하는 것도 모범 사례
    - 아직 완료되지 않은 기능과 함께 핫픽스를 푸시하면 안됨

### Create a branch

- branch를 생성하려면
    
    → 상단 메뉴바에서 Version Control > Manage branch lines 클릭
    
- 브랜치를 생성하는 3가지 방법
    - Revisions of the mainline(메인라인을 개정)
    - Revisions of another branch line(다른 브랜치 라인을 개정)
    - Tagged versions(태그된 버전)

### Merge changes

****Port fix (only available on mainline)****

- 포트 수정은 브랜치 라인 중 하나에서 메인라인으로 특정 부품을 이동할 수 있는 옵션을 제공
- 단일 기능을 브랜치에서 프로덕션으로 이동하는 예외적인 경우에 이 작업을 수행할 수 있음
- 필요한 기능을 선택하려면 하나 또는 여러 개정판을 선택할 수 있음
- Mendix 모범 사례로 인해 이 옵션은 자주 사용되지 않음
- 다음 섹션에서 설명하는 전체 분기만 이동하는 것이 좋음

**Merge feature branch (only available on mainline)**

- 이 기능은 전체 분기를 메인라인에 병합하는 데 사용되며 메인라인에서만 사용할 수 있음
- 일반적으로 브랜치 라인의 개발이 완료되면 브랜치 라인을 메인라인에 병합됨
- 병합 작업을 시작하려면 Studio Pro에서 메인라인을 연다.
    
    → 상단 메뉴바 > Version control > Merge Changes Here 클릭
    
- 참고 : Merge하기 전에 메인라인에서 모든 변경 사항을 커밋해야 함
- 메인라인에 병합하려는 기능 브랜치를 선택
- 선택하면 branch line에 적용된 변경 사항이 변경 사함 도킹에 나열됨
    
    → 이는 팀 서버 버전과 로컬 버전 간의 차이를 나타냄
    
- 이러한 변경 사항을 메인라인에 커밋한 후, 브랜치를 메인라인에 성공적으로 병합함

**Advanced merge (available on mainline and branch lines)**

- **Advanced merge**을 사용하면 본선 또는 지선의 다양한 개정판을 각각 선택한 선 유형에 병합할 수 있음

****Reverse merge changes****

- 병합된 변경 사항은 되돌릴 수 있음
    
    → 이를 위해서는 변경 사항을 되돌리는 데 사용될 시작 버전과 최종 버전이 무엇인지 표시해야 함
    
- 한 번에 여러 커밋을 롤백할 수 있지만 시작 및 끝 개정에 대해 동일한 개정을 선택하여 단일 커밋만 되돌리도록 선택할 수 있음

****Delete a branch****

- 분기가 다른 분기 또는 메인라인에 병합된 후 해당 분기 라인을 삭제할 수 있음
- 사용하지 않는 분기를 정리하면 분기를 제어하는 데 도움이 됨
- 지점을 선택하고 삭제를 확인하면 지점을 삭제할 수 있음

## ****Using Your Own SVN server****

- 기본적으로 Mendix는 Team Server를 활성화할 때, SVN 환경 프로비저닝을 관리함
    
    → SVN(SubVersion) : 여러명이서 작업하는 프로젝트 버전 관리나 각자 만든 소스의 통합과 같은  문제를 해결하기 위해 저장소를 만들어 그 곳에 소스를 저장해 소스 중복이나 여러 문제를 해결하기 위한 형상 관리(소스의 변화를 끊임없이 관리하는 것)/소스 관리 툴
    
    → 프로비저닝 : 사용자가 요청한 IT 자원을 사용할 수 있는 상태로 준비하는 것
    
- 이를 통해 가동 시간 극대화에 초점을 맞춘 일일 백업 및 운영 처리로 인해 방해 받지 않으면서 통제력을 유지 가능
- 앱 배포 디렉토리를 저장할 수도 있음
    
    → 이를 위해서는 먼저 자체 SVN 서버를 설정해야 함
    
    → Studio Pro > Edit > Preferences > Version Control > Enable private version control
    
    → Version Control > item Upload to Version Control Server 항목의 추가 옵션에 대해 이제 개인 서버 옵션을 사용할 수 있음
    
    → 여기에 저장소 주소를 입력하여 구성을 완료할 수 있음
    

## 요약

- 버전 관리 시스템에서 제공하는 다양한 옵션
- Mendix 앱에 팀 서버를 사용하는 것이 권장되는 이유