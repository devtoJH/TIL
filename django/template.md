# Template System

## django template system
    데이터 표현을 제어하면서, 표현과 관련된 로직을 담당

## (DTL)Django Template Language
    Template에서 조건, 반복, 변수, 필터 등의 프로그래밍적 기능을 제공하는 시스템

## DTL Syntax
1. Variable
2. Filters
3. Tags
4. Comments

### Variable
- view 함수에서 render 함수의 세 번째 인자로 딕셔너리 타입으로 넘겨 받을 수 있음
- key에 해당하는 문자열이 template에서 사용 가능한 변수명이 됨
- dot(.)를 사용하여 변수 속성에 접근할 수 있음

### Filters
- 표시할 변수를 수정할 때 사용
- chained가 가능하며 일부 필터는 인자를 받기도 함
- 약 60개의 필터를 제공

```python
{{ variable|filter }}
```

### Tags
- 반복 또는 논리를 수행하여 제어 흐름을 만드는 등 변수보다 복잡한 일들을 수행
- 일부 태그는 시작과 종료 태그가 필요
    ```python
    {% if %} {% endif %}
    ```
- 약 24개의 태그를 제공

```python
    {% tag %}
```

### Comments
- DTL에서의 주석 표현

 ```html
<h1>Hello, {# name #}</h1>
```
```python
{% comment %}
{% endcomment %}
```

# template 상속
    - 페이지의 공통 요소를 포함하고, 하위 템플릿이 재정의 할 수 있는 공간을 정의하는
    - 'skeleton' 템플릿을 작성하여 상속 구조를 구축

```html
<!-- skeleton 역할 템플릿 작성 -->

<!DOCTYPE html>
<html lang="en">
<head>
    ...
</head>
<body>
    {% block content %}
    {% endblock content %}
</body>
</html>
```

## 'exends' tag
- 자식(하위)템플릿이 부모 템플릿을 확장한다는 것을 알림
- **반드시 템플릿 최상단에 위치할 것!(2개 이상 사용 불가)**

```python
{% extends 'path' %}
```

## 'block' tag
- 하위 쳄플릿에서 재정의(overridden)할 수 있는 블록을 정의
- 하위 템플릿이 작성할 수 있는 공간을 지정

```python
{% extends 'path' %}
```

# 요청과 응답 with HTML form

## 데이터를 보내고 가져오기

### 'form' element
- 사용자로부터 할당된 데이터를 서버로 전송
- 웹에서 사용자 정보를 입력하는 여러 방식(text, password 등)을 작성
- form 데이터는 **HTTP request** 객체에 들어있음(view 함수의 첫번째 인자)

### 'action' & 'method'
- form의 핵심 속성 2가지
- "데이터를 어디(**action**)로 어떤 방식(**method**)으로 보낼지"

#### 1. action
- 입력 데이터가 전송될 url을 지정(목적지)
- 만약 이 속성을 지정하지 않으면 데이터는 현재 form이 있는 페이지의 url로 보내짐

#### 2. method
- 데이터를 어떤 방식으로 보낼 것인지 정의
- 데이터의 HTTP request methods (GET, POST)를 지정

### 'input' element
- 사용자의 데이터를 입력 받을 수 있는 요소
- type 속성 값에 따라 다양한 유형의 입력 데이터를 받음

### name
- input의 핵심 속성
- 데이터를 제출했을 때 서버는 name 속성에 설정된 값을 통해<br>
사용자가 입력한 데이터에 접근할 수 있음

## Query String Parameters
- 사용자의 입력 데이터를 url 주소에 파라미터를 통해 넘기는 방법
- 문자열을 앰퍼샌드(&)로 연결된 key=value 쌍으로 구성되며, 기본 url과 물음표(?)로 구분됨
- 예시
    - http://host:port/path?**key=value**&**key=value**


---
<br>

# 참고

## DTL 주의사항
- python처럼 일부 프로그래밍 구조(if, for 등)를 사용할 수 있지만<br>
명칭을 그렇게 설계했을 뿐 
- python 코드로 실행되는 것이 아니며, python과 아무런 관련이 없음
- 프로그래밍적 로직이 아니라 프레젠테이션을 표현하기 위한 것임을 명심
    - 프로그래밍적 로직은 되도록 view 함수에서 작성 및 처리

## DTL 학습
- 공식문서 참고(태그, 필터)
    - https://docs.djangoproject.com/en/3.2/ref/templates/builtins/