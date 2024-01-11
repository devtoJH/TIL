# The App Directory

## Locating the App Directory

- 해당 앱 디렉토리를 찾기
    - 상단 앱 메뉴(App) → 탐색기에 앱 디렉토리 표시 옵션을 선택(Show App Directory in Explorer) → Window 탐색기 열림 → 이 앱에 속한 파일과 폴더가 표시됨

## The Clean Directory Example

- 맨 처음 앱 디렉토리의 폴더는 앱 디렉토리의 ‘clean’ 버전(처음으로 열리는 새 앱)임

- Javascriptsource
    - Javascriptsource 폴더 내에서 앱 모듈과 구조와 유사한 구조를 찾을 수 있지만 nanoflows에 대해 실제 JavaScript 작업이 정의된 모듈만 있음
    - 해당 모듈에 속한 모든 JavaScript 소스를 쉽게 찾을 수 있으며 다른 앱에서 이 모듈을 재사용할 수 있음
    
- Javasource
    - Javasource 폴더 내에서 앱 모듈의 구조와 유사한 구조를 찾을 수 있음
    - 해당 모듈의 microflow에 속하는 모든 Java 소스가 포함임
    - 새 앱에는 이제 디렉토리에 반영된 9개의 모듈이 있음

- 참고
    - 경우에 따라 사용자 정의 코드를 구현하는 타사 Java 파일로 연결되는 하위 폴더가 있는 동일한 디렉토리 수준에서 다른 폴더를 찾을 수 있음
    - Apache 라이브러리를 생각해 볼 것

- 모듈 폴더의 하위 폴더들
    - Actions
        - Actions 폴더는 해당 특정 모듈에서 생성된 모든 Java 작업의 Actions 폴더임
        - 이는 Studio Pro에서 수행하는 작업
        - 현재 Actions 폴더에 있어야 하는 유일한 파일은 **VerifyPassword.java**임
        - 이는 현재 시스템 모듈에 있는 단일 Java 작업을 반영함
    
    - Datasets
        - Datasets 폴더는 해당 특정 모듈에서 생성된 모든 Datasets의 대상 폴더임
        - 이는 Studio Pro에서 수행하는 작업
        - 현재 폴더는 비어 있어야 하지만 Datasets 파일을 생성하고 Java 작업을 해당 소스로 선택하여 디렉토리에도 생성되었는지 확인할 수 있어야 함
        - OQL 쿼리를 소스로 선택하면 OQL 코드가 모델에서 유지 관리되므로 디렉토리에 이 Datasets에 대한 파일이 표시되지 않음
    

## Create Dataset

1. MyFirstModule 모듈에 데이토 세트를 생성하고 **EnrolledCandidatesReport**라는 이름을 지정한다
2. 이것이 생성되면 앱 디렉토리를 개방형 모델과 동기화해야 함
    1. 상단 메뉴바에서 앱 메뉴(App)를 열고 앱 디렉토리 동기화(Synchronize App Directory)를 선택
    2. F4를 눌러 동일한 작업을 빠르게 수행 가능함
3. 이제 App Directory/javasource/myfirstmodule/datasets/ 경로를 따르면 앱 디렉토리에서 파일을 볼 수 있음

## The Clean Directory Example - Continued

- 앱 디렉토리 폴더의 하위 폴더들
    - Proxies
        - 시스템 모듈의 디렉토리로 다시 전환하여 proxies 폴더의 내용을 살펴보면 microflow라는 폴더 하나, Constants 폴더 및 여러 파일이 있음
        - proxies 폴더는 모든 엔터티, 영구, 비영구 및 모든 열거와 유사함
        - 내부 microflow 폴더에는 해당 모듈의 모든 microflow 이름을 저장하는 Microflows.java라는 파일이 하나 있음
            
            → 이는 Java 개발을 수용하기 위한 것
            
        - constants 폴더와 Constants.java파일에도 동일하게 적용됨
    
    - Resources
        - 한 단계 위로 올라가면 리소스 폴더에서 HTML 파일이나 구성 파일과 같이 애플리케이션 작동 방식에 직접적인 영향을 미치는 파일만 찾아야 함
        - 앱 모델과 함께 패키징 됨
        - 해당 폴더의 파일은 Java 리소스로 액세스할 수 있음
        - 이 폴더를 활용하는 Mendix 모듈의 예로는 SAML 모듈과 Deeplink 모듈이 있음
    
    - Theme
        - 테마 폴더에는 애플리케이션 스타일의 소스를 함께 구성하는 파일과 폴더가 있음
        - 이 폴더를 변경하려면 HTML/CSS/SASS 지식이 필요함
        - 이러한 지식을 바탕으로 기존 디자인 속성을 확장 또는 변경하거나 새로운 디자인 속성을 생성할 수 있음
    
    - Userlib
        - userlib 폴더에서는 사용자 정의 Java 기능을 지원할 수 있는 Java 라이브러리를 찾을 수 있음
        - 커뮤니티와 같은 모듈을 다운로드하면 이 폴더의 내용이 변경됨
        - [Commons Function Library](https://marketplace.mendix.com/link/component/170) 또는 [템플릿이 포함된 이메일 모듈](https://marketplace.mendix.com/link/component/259)
        - 다운로드한 기능을 더 이상 사용하지 않는 한 이 파일을 변경하지 말 것
        - 모듈을 제거해도 Java 라이브러리는 이 디렉토리에서 자동으로 제거되지 않으므로 제거하는 것을 잊지 말 것
    
    - Widgets
        - 위젯 폴더에는 확장자가 .mpk인 찾기 파일만 포함되어 있음
        - 이러한 파일은 Studio Pro에서 사용할 수 있는 위젯을 반영함
        - 추가 기능 위젯 그룹에 나열된 위젯 수는 앱 디렉토리의 파일 수와 다를 수 있음
            
            → 이는 .mpk 파일이 여러 위젯을 반영할 수 있기 때문
            
            → 이 예로 영역 차트, 막대 차트, 버블 차트 및 기타 몇 가지 차트가 포함된 Chart.mpk가 있음
            
        - 위젯 구축 방법을 알고 있는 경우에만 파일을 변경할 것
            
            → 이를 위해서는 Mendix API 및 JavaScript 프로그래밍 언어에 대한 지식 필요
            
    
    - Files in this folder
        - 가장 높은 수준(루트 폴더)의 항목 옆에 앱 디렉토리에는 아래와 같은 파일이 있음
            - .mpr
                - Studio Pro가 앱을 열 때 필요한 <AppName>.mpr 파일
                
            - .mpr.bak
                - <AppName>.mpr.bak 파일은 <AppName>.mpr 파일의 백업 파일
                - 문제가 발생할 경우 백업을 사용하여 앱을 복원할 수 있음
                - 이런 일이 발생할 수 있는 2가지 순간
                    1. Mendix 버전을 업그레이드
                    2. Team Server 앱을 업데이트
            
            - .mpr.lock
                - <AppName.mpr.lock 파일은 이 앱이 현재 Studio Pro에 열려 있음을 나타냄
                - 이 파일은 Windows 설정에 따라 숨겨질 수 있음

## Optional Files and Folders

- 앱 배포, 데이터 스냅샷 생성, Marketplace 모듈 가져오기 등 Studio Pro에서 작업을 수행하면 앱 디렉토리가 변경됨

- Deployment folder
    - 배포 폴더에는 앱을 로컬에서 실행하는 데 필요한 배포 파일이 포함되어 있음
    - 이 폴더에는 로컬 데이터베이스를 활용하는 데 필요한 여러 폴더와 파일, 애플리케이션 사용 중에 저장된 파일, Mendix가 애플리케이션을 실행하기 위해 해석한 소스가 포함되어 있음

- Releases folder
    - Studio Pro를 통해 배포 패키지를 생성할 때 Mendix는 기본적으로 해당 패키지를 releases 폴더에 저장
    
- Packages folder
    - 앱 패키지를 생성할 때 Mendix는 이러한 패키지를 저장할 위치를 자동으로 제공함
    - 패키지 폴더에는 생성된 패키지가 저장됨

- data-snapshot.zip file
    - Studio Pro를 통해 데이터 스냅샷을 생성하면 데이터 스냅샷 파일이 생성됨
    - 여기에는 팀원이 재사용할 수 있는 로컬 데이터 베이스가 포함되어 있음

- .classpath file
    - Eclipse가 앱을 이 애플리케이션으로 가져오는데 필요한 파일

- .app file
    - Eclipse가 앱을 이 애플리케이션으로 가져오는데 필요한 파일

- <root folder>.launch file
    - Eclipse가 앱을 이 애플리케이션으로 가져오는데 필요한 파일

## Best Practices

- 앱 디렉토리를 깨끗하고 최신 상태로 유지하는 것은 매우 중요함
- 작업의 결과로 이 디렉토리의 컨텐츠가 변경되면 어떤 모듈과 위젯을 추가하는지 파악하고 더 이상 사용하지 않는 경우 앱 디렉토리에서 적시에 제거할 것
    1. 모듈을 제거할 때 userlib 폴더에서 Java 라이브러리를 수동으로 제거해야 함
    2. 리소스 폴더의 컨텐츠가 배포 폴더의 모델/리소스 폴버에 복사됨, 배포 폴더에 추가할 수 없는 모든 파일은 이 리소스 폴더에 추가할 수 있음
    3. 다음 모듈에서 설명할 버전 관리를 사용하는 경우 커밋하기 전에 앱을 업데이트하여 새로운 기능이나 충돌을 확인하고 해결할 것

## 요약

- Mendix 앱의 앱 디렉토리가 어떻게 구성되어 있는지
- 이것이 Studio Pro의 앱 컨텐츠와 어떻게 관련되는지
- 앱 디렉토리의 컨텐츠가 수정되는 결과를 초래하는 작업에 대해