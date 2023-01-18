## 객체(object)
    객체(object)는 특정 차입의 인스턴스(instance)이다.
- 123, 50, 7는 모두 int의 인스턴스
- 'hello', 'bye'는 모두 string의 인스턴스
- [232, 89, 1], []은 모두 list의 인스턴스

### 객체 특징
- 타입 : 어떤 연산자와 조작이 가능한가?
- 속성 : 어떤 상태(데이터)를 가지는가?
- 조작법 : 어떤 행위(함수)를 할 수 있는가?

### 객체지향 프로그래밍
- 프로그램을 여러 개의 독립된 객체들과 그 개체들 간의 상로작용으로 파악하는 프로그래밍 방법
- 데이터와 함수로 인한 변화
- 데이터와 기능(메서드) 분리, 추상화된 구조(인터페이스)
---
- 사각형 - 클래스(class)
- 각 사각형(R1, R2) - 인스턴스(instance)
- 사각형의 정보 - 속성(attribute)
    - 가로, 세로 길이
- 사각형의 행동 / 기능 - 메서드(method)
    - 넓이, 높이를 구한다.

### 객체지향의 장점
- 프로그램을 유연하고 변경이 용이함
- 소프트웨어 개발과 보수를 간편하게 하고 직관적인 코드 분석을 가능하게 한다.

## 클래스
```python
# 클래스의 정의
class MyClass:
    pass

# 인스턴스 생성
my_instance = MyClass()
# 메서드 호출
my_instance.my_method()
# 속성
my_instance.my_attribute
```
- 객체의 틀(클라스 = 붕어빵 틀)을 가지고, 객체(인스턴스 = 붕어빵)를 생성한다.
- 클래스 : 객체들의 분류(class)
- 인스턴스 : 하나하나의 실체 / 예(instance)
- **파이썬은 모든 것이 객체, 모든 객체는 특정 타입의 인스턴스**

### 속성
- 특정 데이터 타입/클래스의 객체들이 가지게 될 상태/데이터를 의미

### 메서드
- 특정 데이터 타입/클래스의 객체에 공통적으로 적용 가능한 행위(함수)

### 객체 비교하기
- ==
    - 동등한(equal)
    - 변수가 참조한느 객체가 동등한(내용이 같은) 경우 True
    - 두 객체가 같아 보이지만 실제로 동일한 대상을 가리키고 있다고 확인해 준 것은 아님
- is
    - 동일한(equal)
    - 두 변수가 동일한 객체를 가리키는 경우 True
```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b, a is b)
# True False

a = [1, 2, 3]
b = a

print(a == b, a is b)
# True True
```

## 인스턴스
### 인스턴스 변수
- 인스턴스가 개인적으로 가지고 있는 속성
- 각 인스턴스들의 고유한 변수
- 생성자 메서드에서 self.<name>으로 정의
- 인스턴스가 생성된 이후 <instance>.<name>으로 접근 및 할당

### 인스턴스 메서드
- 인스턴스 변수를 사용하거나, 인스턴스 변수에 값을 설정하는 메서드
- 클래스 내부에 정의되는 메서드의 기본
- 호출 시, 첫 번째 인자로 인스턴스 자기자신(self)이 전달됨
```python
class MyClass
    def instance_method(self, arg1, ...)
```

### self
- 인스턴스 자기자신
- 파이썬에서 인스턴스 메서드는 호출 시 첫 번째 인자로 인스턴스 자신이 전달되게 설계
    - 매개변수 이름으로 self를 첫 번째 인자로 정의
    - 다른 단어로 사용 가능하나, 파이썬의 암묵적인 규칙

### 생성자(constructor) 메서드
- 인스턴스 객체가 생성될 때 자동으로 호출되는 메서드
- 인스턴스 변수들의 초기값을 설정
    - 인스턴스 생성
    - __init__메서드 자동 호출

### 소멸자(destructor) 메서드
- 인스턴스 객체가 소멸(파괴)되지 직전에 호출되는 메서드

### 매직 메서드
- 특수한 동작을 위해 만들어진 메서드로 스페셜 메서드 혹은 매직 메서드라고 불림

### 매직 메서드 예시
- 객체의 특수 조작 행위를 지성(함수, 연산자등)
    ```python
    __str__ : 해당 객체의 출력 형태를 지정
        - 프린트 함수를 호출할 때, 자동으로 호출
        - 어떤 인스턴스를 출력하면 str의 return값이 출력
    __gt__ : 부등호 연산자(>, greater than)
    ```
- 종류
    ```python
    __str__(self), __len__(self), __repr__(self)
    __it__(self, other), __le__(self, other), __eq__(self, other)
    __gt__(self, other), __ge__(self, other),__ne__(self, other)
    ```