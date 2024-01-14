# Using Simple Constraints

## 서론

- 이번 모듈에서는 휴가 요청 애플리케이션을 구축하기 위해 강의 실습할 예정
- 데이터와 상호 작용하기 위해 기본 XPath를 작성하는 방법을 학습할 계획
    
    → 애플리케이션의 핵심을 구축하고 사용자에게 휴가 요청을 생성할 수 있는 공간을 제공
    
- 이 모듈에서 진행할 것
    - 열거형 값을 사용하여 데이터 제한
    - Mendix 시스템 변수를 사용하여 제한
    - XPath 제약 조건을 사용하여 보안 규칙 적용

## 휴가 요청 앱 구축 시작

- 지난 모듈에서는 휴가 요청을 추적하는 사용 사례를 소개함
    - 회사에는 휴가 요청을 제출, 검토 및 승인하는 방법이 필요함
    - 직원은 휴가 요청을 생성할 수 있어야 하고, 관리자(Managers)는 직속 부하 직원 요청을 승인할 수 있어야 함
    - 보안 데이터는 매우 중요하므로 직원이 자신의 요청만 볼 수 있도록 해야 함
    - 관리자(Managers)는 직속 부하 직원의 요청만 관리할 수 있어야 함
    - 관리자(Administrator)는 모든 직원과 관리자(Managers)의 요청을 볼 수 있어야 함. 또한, 각 요청을 승인할 관리자(Managers)를 지정하는 일도 담당해야 함

### 도메인 모델 구축

- 이 앱을 구동하는 중심 개체는 휴가 요청임
- 이 객체에는 휴가 시작 시기, 종료 시기, 휴가 상태, 설명, 휴가 요청 요청자 및 승인자에 대한 연결과 같은 주요 정보가 포함되어야 함
- 엔터티 이름을 VacationRequest라 정하고 다음 속성을 설정할 것
    - Description - String
    - StartDate - DateTime
    - EndDate - DateTime
    - • Status – Make a new Enumeration ENUM_VacationRequestStatus with values: ‘Draft’, ‘Submitted’,‘Approved’, and ‘Rejected’
- Association 탭에서, 다음 연결에서 VacationRequest 엔터티를 Administration.Account 엔터티로 확장할 것
    - • One-to-many association, name it *VacationRequest_Submitter*
    - • One-to-many association, name it *VacationRequest_Approver*

### Home Page

- 사용자가 제출한 휴가 요청과 해당 요청의 현재 상태가 표시됨
- 또한, 사용자가 휴가 요청을 생성하거나 편집할 수 있는 페이지를 생성함

**홈페이지 구축**

1. 컨테이너에 Data grid 드래그한다
    - 이를 사용하여 사용자가 제출한 모든 휴가 요청을 표시한다
2. Data grid에서 Data Source 탭에서 XPath로 설정한다
    - Data grid의 내용을 자동으로 채울지 묻는 메세지가 나타난다면 ‘Yes’를 선택한다
3. 방금 생성한 Data grid에서 새로 만들기 버튼을 선택한 후, 마우스 오른쪽 버튼을 클릭한다
    - New 버튼과 Edit 버튼에 우클릭하여 메뉴에서 **Generate page…**를 선택한다
4. 페이지 만들기 메뉴가 나타나게 된다(아래의 순서를 따를 것)
    - Name the page **VacationRequest_NewEdit**.
    - Use the **Atlas_Default** Navigation Layout.
    - Select the **Form Vertical** page layout.
    - Click **OK** to create this page.
5. 페이지를 우클릭하고 속성(Properties)을 선택하여 사용자(User) 및 관리자(Manager) 역할에 **VacationRequest_NewEdit** 페이지를 볼 수 있는 권한을 부여한다

- 이를 통해 사용자는 애플리케이션에 로그인하고 스스로 휴가 요청을 작성할 수 있음
- 그러나 현재 홈 페이지에는 연령이나 상태에 관계없이 모든 요청이 표시됨
- 비즈니스 요구 사항을 더 잘 충족하기 위해 상태 열거(Enumeration)의 XPath를 활용하여 제출된 요청에 대한 대시보드와 이전 요청 아카이브를 구축할 예정임
- 읽기/쓰기 액세스로 인해 오류가 나타날 수 있음

## 열거(Enumeration)가 무엇인가요?

- [열거](https://docs.mendix.com/refguide/enumerations/)는 사전 정의된 문자열 값 목록이 있는 속성이다
- 드롭다운이나 라디오 버튼을 통해 선택할 수 있으며 데이터 일관성을 쉽게 유지할 수 있음
- 데이터베이스 수준에서 열거형은 단순히 문자열이다
- Mendix 플랫폼은 열거형 값으로 XPath를 생성할 때 지원을 제공함

## 열거형을 사용하여 데이터 제한

- 더 나은 대시보드를 제공하기 위해 ‘제출된’요청과 ‘아카이브’ 탭 내의 다른 모든 유형만 표시하도록 홈 화면의 보기를 제한한다
    
    → 이를 수행하려면 ‘상태’ 열거를 사용해야 함
    
    1. 그리드(탭 컨테이너 박스안의 데이터 그리드 선택) 속성 창에서 데이터 소스 탭을 연다
        1. 이 창은 데이터 그리드를 우클릭하고 속성을 선택하면 찾을 수 있음
    2. XPath 제약 조건 편집기 창을 사용하여 ‘제출됨’ 상태에 있는 VacationRequest 엔터티만 반환하는 XPath를 작성할 것
        
        → 이를 수행하는 가장 쉬운 방법은 ‘**[**’로 입력을 시작하여 자동 편집기를 불러오는 것
        
        → ‘Status’를 입력하기 시작하면 해당 속성이 옵션으로 표시되는 자동 완성 드롭다운이 표시됨
        
        → 이를 선택하고 ‘**=**’를 추가하면 자동 완성 창이 다시 표시됨
        
        → 이 창의 시스템 변수 아래에는 자동 완성 창에 가능한 모든 열거 값이 표시되어 XPath를 완료하는 데 도움이 됨
        
    3. 결국 그리드를 올바르게 필터링하는 XPath 제약 조건은 다음과 같아야 함
        
        → *[Status = ‘Submitted’]*
        
    
- 이때, 그리드는 생성되지만 여전히 애플리케이션을 실행시킬 수 없음
- 오류 창에는 사용자의 보안 역할이 누락되었다는 메시지가 표시됨
- 보안 애플리케이션을 구축하려면 데이터에 대한 적절한 액세스 권한을 부여하는 XPath 기반 보안 규칙을 생성해야 함

## Mendix 시스템 변수 사용

- 자동 완성 열거 외에도 Mendix 플랫폼에는 XPath 생성에 사용할 수 있는 다양한 시스템 변수가 있음
- 여기에는 현재 사용자, 사용자 역할, 현재 세션, 날짜 및 시간에 대한 참조가 포함되어 데이터를 더 효과적으로 제어할 수 있음
- 이러한 변수는 항상 ‘**[%**’ 문자로 시작하며 **Ctrl + Space** 자동 완성 메뉴를 사용하여 찾을 수 있음
- 가장 유용한 시스템 변수 중 두 가지는 **'[%CurrentObject%]'** 및 **'[%CurrentUser%]'**이다

*참고 : XPath 변수의 전체 목록은 [XPath 키워드 및 시스템 변수 참조](https://docs.mendix.com/refguide/xpath-keywords-and-system-variables/) 자료를 참고할 것*

**CurrentObject**

- [%CurrentObject%] 변수는 현재 컨텍스트 개체의 고유 식별자를 나타냄
    
    → 실제로 이는 데이터 보기 내에 포함된 Data Grid의 경우 ‘**[%CurrentObject%]’**가 Data View의 개체를 나타냄을 의미함
    
- 데이터 보기의 개체를 컨텍스트 개체라고 함
    - 컨텍스트 개체가 없으면 이 변수는 자동 완성 메뉴에 표시되지 않음

**CurrentUser**

- CurrentObject와 마찬가지로 Mendix 플랫폼은 애플리케이션의 현재 사용자를 참조하는 빠른 방법을 제공함
    - 이는 Ctrl + Space 드롭다운 메뉴에 있는 ‘[%CurrentUser%]’ 변수를 통해 수행됨
    - ‘[%CurrentUser%]’는 XPath가 사용되는 모든 위치에서 사용할 수 있음
        - 이는 보안 제약 조건을 생성할 때도 유용하며, 우리는 이를 활용하여 앱을 보호할 것임

*참고 : 예약된 이벤트 및 시작 후 마이크로플로우와 같은 시스템 프로세스에서는 ‘[%CurrentUser%]’ 변수를 사용하지 말 것. 그 시간에는 사용자가 없을 것임*

## Mendix 시스템 변수를 사용하여 제한

- 보다 안전한 앱을 구축하기 위해 XPath 보안 규칙을 추가한다
    - 이를 위해, 도메인 모델의 VacationRequest_Submitter 관계를 활용한다
- 이 작업을 수행하기 전에 해당 사용자가 요청을 생성할 때 애플리케이션이 VacationRequest_Submitter 연결을 현재 사용자로 설정하는지 확인하고 싶음
- 이를 위해 홈 페이지의 ‘새로 만들기’ 버튼을 마이크로플로우를 호출하는 버튼으로 대체
    - 이 마이크로플로우의 목표는 다음과 같다
        - Retrieve the current user’s account using the ‘[%CurrentUser%]’ variable
        - Create a new VacationRequest object
        - Set the VacationRequest_Submitter association to the user’s account
        - Show the VacationRequest object on a page

- 위와 같은 방법을 하기 위한 방법은 다음과 같다
    1. 이 마이크로플로우를 사용하려면 먼저 마이크로플로우를 트리거하는 버튼을 추가해야 함
        1. 홈페이지를 열고, 데이터 그리드에는 데이터 그리드 컨트롤 막대에 ‘새로 만들기’라는 라벨이 붙은 만들기 버튼이 있음
        2. 단순히 개체를 만드는 것 이상의 작업을 수행하려면 이 버튼을 삭제하고 대신 새 작업 버튼을 추가한다
    2. 버튼을 두 번 클릭하여 버튼 속성을 연다
        1. Caption → New, Events/On Click → Call a microflow로 변경
        2. 아직 마이크로플로우를 작성하지 않았으므로, New 버튼 클릭
        3. 마이크로플로우의 이름을 **ACT_VacationRequest_Create**로 정하고 OK 클릭
    3. ACT_VacationRequest_Create을 연다.
        1. 마이크로플로우가 사용자가 데이터 그리드에서 행을 선택하고 VacationRequest 객체를 흐름에 전달할 것으로 예상함을 나타내는 VacationRequest 입력이 정의되어 있음
        2. 그래서 New 버튼을 눌러 새로운 휴가 요청을 생성하면 아직 전달할 객체가 없어 오류가 발생하게 됨
    4. 해당 오류를 방지하려면 VacationRequest(매개변수)를 삭제한다
    5. Retrieve 활동을 추가한다
        1. Set the Retrieve Source to be **From database**
        2. Retrieve the **Administration.Account** Entity
        3. Under the options for **Range** select **First**
        4. Create an XPath constraint that sets the **id** to be equal to the ‘**[%CurrentUser%]**’
    6. Create object를 추가한다
        1. 이 활동에서는 VacationRequest를 엔터티로 설정하고 VacationRequest_Submitter 연결을 검색된 계정으로 설정한다
            - Entity → VacationManagement.VacationRequest, Commit 및 Refresh → No, 하단에 New버튼을 클릭해 Member → VacationManagement.VacationRequest_Submitter, Member type → Administration.Account, Type → Set, Value → $Account로 설정할 것
    7. Show Page를 추가하고 이전에 생성된 VacationRequest_NewEdit 페이지를 열도록 설정한다
        1. Mendix는 이 마이크로플로우에 휴가 요청 입력 매개변수를 자동으로 넣는다
            
            → 이는 휴가 요청 개체 그리드에서 이 마이크로플로우를 생성했기 때문
            
        2. 이 마이크로플로우에는 입력 매개변수가 필요하지 않음
        3. ‘Object to pass’가 필요하며 이를 NewVacationRequest로 설정한다
    8. 모든 모듈 역할에 **ACT_VacationRequest_Create**에 액세스할 수 있는 권한을 부여해야 하는 것을 잊지 말 것

## XPath를 사용하여 보안 규칙 설정

- 우리는 애플리케이션 사용자가 스스로 새로운 요청을 생성하고 설명, 시작 날짜 및 종료 날짜를 입력할 수 있기를 원함
- VacationManagement 모듈의 보안 메뉴를 사용하여 VacationRequest 엔터티에 대한 엔터티 액세스를 설정한다
    1. VacationManagement 모듈의 보안 메뉴로 이동한다
        1. Module roles의 탭에서 New 버튼을 클릭해 ‘**Administrator**’라는 이름을 작성한 후, OK를 클릭한다
    2. Navigate 메뉴를 클릭해 Entity Access 탭으로 이동한다
        1. New 버튼을 클릭해 Access Rule를 추가한다
        2. 그럼 엔터티를 선택할 수 있는 창이 나타나는데, VacationRequest 엔터티를 선택한다
        3. Role이 적용될 모듈 역할의 확인란 목록에서 사용자 역할을 선택한다
            - 다음 액세스 규칙을 정의한다
                - Description – Read, Write
                - StartDate – Read, Write
                - EndDate – Read, Write
                - Status – Read
                - Vacationrequest_Submitter – Read
                - VacationRequest_Approver – Read
        4. 새 객체 생성 허용(Allow creating new objects) 및 기존 객체 삭제 허용(Allow deleting existing objects) 확인란을 선택한다
        5. 마지막 부분은 사용자가 자신이 제출자인 요청만 볼 수 있도록 VacationRequest에 대한 액세스를 제한하는 것임
    3. XPath constraint 탭으로 이동한다
        
        → 이 탭에는 현재 사용자를 문제의 개체에 연결하는 연결을 선택하는 데 도움이 되는 사용자 경로하는 버튼이 포함되어 있음
        
        - 시작하려면 ‘**[**’를 눌러 XPath 자동 완성 메뉴를 불러온다
        - 닫혀 있으면 **Ctrl + Space**를 눌러 다시 불러온다
        - XPath constraint는 다음과 같아야 한다
            
            → *[VacationManagement.VacationRequest_Submitter=’[%CurrentUser%]’]*
            
        - 작성을 완료했다면 OK를 클릭한다
    4. 관리자(Managers)는 자신이 승인자인 휴가 요청만 볼 수 있기를 원한다
        1. 동일한 Entity Access 탭에서 방금 생성한 사용자 액세스 규칙을 강조 표시하고 복제 버튼을 누른다
        2. 휴가 요청 구성원에 대한 읽기 권한만 허용하도록 액세스 규칙을 변경하고, 모듈 역할을 관리자로 설정하고, XPath 제약 조건을 변경한다
            
            → *[VacationManagement.VacationRequest_Approver = ‘[%CurrentUser%]’]*
            
    5. 또한 휴가 요청을 생성하고 볼 수 있는 관리자(Administrator)가 필요함
        1. XPath 제약 조건 없이 이 엔터티에 대한 전체 읽기 - 쓰기 및 생성 - 삭제 액세스 권한을 부여하는 관리자 모듈 역할에 대한 VacationRequest 엔터티에 대한 추가 액세스 규칙을 만든다
        2. 첫 번째 반복에서는 관리자가 사용자를 대신하여 요청을 생성해야 하는 경우에 대비해 관리자가 상태를 설정하고 VacationRequest_Submitter 관계를 설정할 수 있기를 원한다
    6. 모든 페이지 및 마이크로플로우에 대한 관리자 액세스 권한을 부여한다
    7. 마지막으로, App Explorer의 App Security 메뉴에서 사용자 역할 관리자에게 VacationManagement 모듈 역할 관리자를 부여한다
        1. 이를 통해 ‘관리자(Administrator)’ 역할을 가진 사용자는 VacationManagement 모듈의 관리자 전용 기능에 액세스할 수 있다
    

## 저장 버튼 교체 및 테스트

- 이 새로운 기능을 테스트하기 전에 요청을 제출하고 상태를 ‘Submitted’으로 변경하는 메커니즘이 필요함
    1. **VacationRequest_NewEdit** 페이지를 열고 왼쪽 하단에서 저장 버튼을 찾는다
    2. 저장 버튼을 우클릭하고, Edit on click action을 클릭한다
    3. Edit action 팝업창에서 On click activity를 Call a microflow를 선택한다
    4. 마이크로플로우 팝업창에서 New 버튼을 클릭한다
    5. 마이크로플로우 이름을 **ACT_VacationRequest_Submit**으로 짓고 OK를 클릭한다
    6. ACT_VacationRequest_Submit 마이크로플로우 창을 열고 다음과 같이 구성한다
        1. Change Object를 드래그한다 (VacationRequest 개체를 변경하기 위해)
            - 이전에 생성한 열거를 사용하여 Status 필드를 ‘Submitted’으로 변경한다
        2. Change Object에서, Commit를 ‘Yes’로 선택한다
        3. 페이지 닫기 작업을 사용하여 페이지를 닫는다. default single을 선택하고 OK를 클릭한다
    7. 모든 모듈 역할에 ACT_VacationRequest_Submit에 액세스할 수 있는 권한을 부여하는 것을 잊지 말 것

- 동일한 마이크로플로우 활동 내에서 VacationRequest를 변경하고 커밋할 수 있다는 점을 기억할 것

**Test it out**

- 애플리케이션을 다시 배포하면 다음이 표시된다
    - 사용자(User)는 자신이 제출한 요청만 홈페이지에서 볼 수 있다
    - 관리자(Managers)는 자신이 직접 생성한 요청이나 승인해야 하는 요청만 홈 페이지에서 볼 수 있다
    - 관리자(Administrators)는 제출된 모든 요청을 확인하고 승인자를 할당할 수 있다

## 요약

- 이 모듈에서는 휴가 요청 애플리케이션의 첫 번째 반복을 빌드하고 다음과 같은 사항을 배움
    - 열거형 값을 사용하여 데이터를 제한하는 방법
    - XPath에서 시스템 변수를 사용하는 방법
    - XPath 제약 조건을 사용하여 보안 규칙을 구성하는 방법