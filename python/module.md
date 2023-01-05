# 모듈(module)
    특정 기능을 하는코드를 파이썬 파일(.py) 단위로 작성한 것
# 패키지(package)
    - 특정 기능과 관련된 여러 모둘의 집합
    - 패키지 안에는 또 다른 서브 패키지를 포함

## 파이선 표준 라이브러리(Python Standard Library, PSL)
- 파이썬에 기본적으로 설치된 모듈과 내장 함수
    - https://docs.python.org/ko/3/library/index.html
    - ex) random.py

### random
    숫자/수학 모듈 중 의사 난수 생성(pseudo random number generator)
    - 대표적으로 임의의 숫자 생성, 무작위 요소의 선택, 무작위 비복원 추출(샘플링)을 위한 함수 제공
- random.randint(a, b)
    - a 이상 b 이하의 임의의 정수 N을 반환
- random.choice(seq)
    - 비어 있지 않은 시퀀스에서 임의의 요소를 반환
    - seq가 비어있으면 indexError를 발생 시킴
- random.shuffle(seq)
    - 시퀀스를 제자리에서 섞음
- random.sample(population, k)
    - 무작위 비복원 추출한 결과인 k 길이의 리스트를 반환

### datetime
    날짜와 시간을 조작하는 객체를 제공
- 사용 가능한 데이터 타입
    - datetime.date, datetime.time, datetime.datetime, datetime.timedelta 등
- datetime.date(year, month, day)
    - 모든 인자가 필수, 인자가 특정 범위에 있는 정수여야 함
    - 이 범위를 벗어나는 인자가 주어지면 ValueError가 발생
- datetime.date.today()
    - 현재 지역 날짜를 반환
- datetime.datetime.today()
    - 현재 지역 datetime을 반환, now()를 활용하면 타임존 설정 가능

### OS
    OS(운영체제)를 조작하기 위한 인터페이스 제공
- os.listdir(path='.')
    - path에 의해 주어진 디렉토리에 있는 항복들의 이름을 담고 있는 리스트를 반환
    - 리스트는 임의의 순서로 나열되며, 특수 항목은 포함하지 않음
- os.mkdir(path)
    - path라는 디렉토리를 만듦
- os.chdir(path)
    - path를 변경

## 에러/예외 처리(Error/Exception Handling)
1. 디버깅
- branches : 모든 조건이 원하는대로 동작하는지
- for loops : 반복문에 진입하는지, 원하는 횟수만큼 실행되는지
- while loops : for loops와 동일, 종료조건이 제대로 동작하는지
- function : 함수 호출시, 함수 파라미터, 함수 결과

2. 에러와 예외
- 문법 에러(Syntax Error)
    - Syntax Error가 발생하면, 파이썬 프로그램은 실행되지 않음
    - 파일 이름, 줄번호, ^ 문자를 통해 파이썬이 코드를 읽어 나갈 때(parser) 문제가 발생한 위치를 표현
    - 줄에서 에러가 감지된 가장 앞의 위치를 가리키는 캐럿(caret)기호(^)를 표시
    - EOL(End of Line), EOF(End of File), Invalid syntax, assign to literal
- 예외(Exception)
    - 실행 도중 예상치 못한 상황을 맞이하면, 프로그램 실행을 멈춤
        - 문장이나 표현식이 문법적으로 올바르더라도 발생하는 에러
    - 실행 중에 감지된느 에러들을 예외(Exception)이라 부름
    - 예외는 여러 타입(type)으로 나타나고, 타입이 메시지의 일부로 출력됨
        - NameError, TypeError 등은 발생한 예외 타입의 종류(이름)
    - 모든 내장 예외는 Exception Class를 상속받아 이뤄짐
    - 사용자 정의 예외를 만들어 관리할 수 있음
    - ZeroDivisionError : 0으로 나누고자 할 때 발생
    - NameError : namespace 상에 이름이 없는 경우
    - TypeError : 타입 불일치
        - TypeError-arguments 부족, TypeError-argument 개수 초과
    - ValueError : 타입은 올바르나 값이 적절하지 않거나 없는 경우
    - IndexError
    - KeyError
    - ModuleNotFoundError : 존재하지 않는 모듈을 import하는 경우
    - ImportError : 모듈은 있으나 존재하지 않는 클래스 / 함수를 가져오는 경우
    - IndentationError : Indentation(들여 쓰기)이 적절하지 않는 경우
    - KeyboardInterrupt : 임의로 프로그램을 종료했을 때

3. 예외 처리
- try문 (statement) / except 절(clause)을 이용하여 예외 처리를 할 수 있음
- try문
    - 오류가 발생할 가능성이 있는 코드를 실행
    - 예외가 발생되지 않으면, except없이 실행 종료
- except문
    - 예외가 발생하면, except 절이 실행
    - 예외 상황을 처리하는 코드를 받아서 적절한 조치를 취함
- 정리
    - try : 코드 실행
    - except : try문에서 예외가 발생 시 실행
    - else : try문에서 예외가 발생하지 않으면 실행
    - finally : 예외 발생 여부와 관계없이 항상 실행함
- 예시
    - 파일을 열고 읽는 코드를 작성하는 경우
        - 파일 열기 시도
            - 파일이 없는 경우 => '해당 파일이 없습니다.' 출력(except)
            - 파일이 있는 경우 => 파일 내용을 출력(else)
        - 해당 파일 읽기 작업 종료 메시지 출력(finally)

4. 예외 발생 시키기
- raise statement => raise <표현식>(메시지)
    - raise를 통해 예외를 강제로 발생
- assert => assert <표현식>, (메시지)
    - assert를 통해 예외를 강제로 발생
    - assert는 상태 검증에 사용되며, 표현식이 False인 경우 : AssertionError
    - 일반적으로 **디버깅 용도**로 사용
- raise VS assert
    - raise : 실제 프로덕션 코드에서 활용
    - assert : 특정 조건이 거짓이면 발생. 디버깅 및 테스트에서 활용
        - -O 옵션으로 실행하는 경우, assert문과 __debug__에 따른 조건부 코드를 제거 후 실행