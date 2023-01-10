# 함수(function)
    - 함수 == 객체
    - 특정한 기능을 하는 코드의 조각(묶음)
    - 코드를 매번 다시 작성하지 않고, 필요 시에만 호출하여 사용

### 함수를 사용해야 하는 이유
1. 코드 중복 방지
2.  재사용 용이

### 함수 기본 구조
1. 선언과 호출(define & call)
2. 입력(input)
3. 범위(scope)
4. 결과값(output)

### 선언과 호출
- 함수의 선언은 def 키워드를 활용함
- 들여쓰기를 통해 function body(실행될 코드 블록)를 작성함
- 함수는 parameter를 넘겨줄 수 있음
- 함수는 동작 후에 return을 통해 결과값을 전달함
- 함수는 함수명()으로 호출
    - parameter가 있는 경우, 함수명(값1, 값2 ...)로 호출
```python
def foo():            foo()
    return True
def add(x, y):        add(2, 3)
    return x + y
```

## 함수의 결과값(Output)
### return
- 함수는 반드시 값을 하나만 return한다.
    -return이 없는 경우에도 None을 반환함
- 함수는 return과 동시에 실행이 종료됨
- 절대로 실행되지 않는 return
```python
def foo(x, y):
    return x - y
    return x * y # => 실행X
foo(4, 5) # -1
#===========================
def foo(x, y):
    return x - y, x * y
foo(4, 5) # (-1, 20)
```
### return VS print
- return은 함수 안에서 값을 반환하기 위해 사용되는 키워드
- print는 출력을 위해 사용되는 함수

## 함수의 입력(Input)
### parameter VS argument
- Parameter : 함수를 실행할 때, 함수 내부에서 사용되는 식별자
- Argument : 함수를 호출할 때, 넣어주는 값
```python
def function(fruit): # parameter : fruit
    return fruit

function('mango') # argument : 'mango'
```
### Argument
    함수 호출 시 함수의 parameter를 통해 전달되는 값
- argument는 소괄호 안에 할당 function_name(argument)
    - 필수 argument : 반드시 전달되어야 하는 argument
    - 선택 argument : 값을 전달하지 않아도 되는 경우는 기본 값이 전달

### position arguments
- 기본적으로 함수 호출 시 argument는 위치에 따라 함수 내에 전달됨

### keyword arguments
- 직접 변수의 이름으로 특정 argument를 전달할 수 있음
- keyword argument 다음에 position argument를 활용 불가능
```python
def add(x, y):        add(x=2, y=5)
    return x + y      add(2, y=5)
```

### Default Argument Values
- 기본값을 지정하여 함수 호출 시 argument 값을 설정하지 않도록 함
    - 정의된 것 보다 더 적은 개수의 argument들로 호출될 수 있음

### 정해지지 않는 개수의 arguments
- 여러 개의 positional argument를 하나의 필수 parameter로 받아서 사용
    - 몇 개의 positional argument를 받을지 모르는 함수를 정의할 때 유용
- argument들을 튜플로 묶여 처리되며, parameter에 *을 붙여 표현
```python
def add(*args):        add(2)
    for arg in args:   add(2, 3, 4, 5)
    print(arg)
```

### 정해지지 않은 개수의 keyword arguments
- 함수가 임의의 개수 argument를 keyword argument로 호출될 수 있도록 지정
- argument들은 딕셔너리로 묶여 처리되며, parameter에 **를 붙여 표현
```python
def family(**kwargs):
    for key, value in kwargs:
    print(key, ":", value)
family(father='John', mother='Jane', me='John Jr.')
```

## 함수의 범위(Scope)
- 함수는 코드 내부에 local scope를 생성하며, 그 외의 공간인 global scope로 구분
- scope
    - global scope : 코드 어디에서든 참조할 수 있는 공간
    - local scope : 함수가 만든 scope. 함수 내부에서만 참조 가능
- variable
    - global variable : global scope에 정의된 변수
    - local variable : local scope에 정의된 변수

### 객체 수명주기
- 객체는 각자의 수명주기(lifecycle)가 존재
    - built-in scope : 파이썬이 실행된 이후부터 영원히 유지
    - global scope : 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
    - local scope : 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지
```python
def fun():
    a = 10
    print('local', a)
fun()
print('global', a)
# local 20
==============
# NameError => a는 local scope에서만 존재
```

### 이름 검색 규칙(Name Resolution)
- 파이썬에서 사용되는 이름(식별자)들은 이름공간(namespace)에 저장되어 있음
- 아래와 같은 순서로 찾아나가며, LEGB Rule이라고 부름
    - Local scope : 함수
    - Enclosed scope : 특정 함수의 상위 함수
    -  Global scope : 함수 밖의 변수, import 모듈
    - built-in scope : 파이썬 안에 내장되어 있는 함수 또는 속성
- 즉, 함수 내에서는 바깥 scope의 변수에 접근 가능하나 수정 불가능
```python
print(sum)
print(sum(range(2)))
sum = 5
print(sum)
print(sum(range(2)))
# <built-in function sum>
1
5
==============
# TypeError: 'int' object is not callable
```

### global 문
- 현재 코드 블록 전체에 적용되며, 나열된 이름(식별자)이 global variable임을 나타냄
    - global에 나열된 이름은 같은 코드 블록에서 global 앞에 등장할 수 없음
    - global에 나열된 이름은 parameter, for 루프 대상, 클래스/함수 정의 등으로 정의되지 않아야 함
- global 예시
    ```python
    In [1]: # 함수 내부에서 글로벌 변수 변경하기
    a = 1
    def fun():
        global a
        a = 3

    print(a)
    fun()
    print(a)
    # 10
    # 3
    ```
- **local scope에서 global 변수 값의 변경, global 키워드를 사용하지 않으면, local scope에 a변수가 생성됨**

## 내장 함수
1. print(*objects, sep=' ',end = '\n') >> 함수를 사용할 때 input으로
    - *objects : *은 여러 값을 무한하게 받을 수 있다.
    - sep = ' ' : sep라는 키워드는 기본 값이 한 칸 space
    - end = '\n' : end라는 키워드는 기본 값이 개행
2. 함수의 반환 값(return)
- print(print('hi')) >> None : print 함수는 반환 값이 없음
- print(sum([1, 2, 3])) >> 6 : sum 함수는 합을 반환함
3. 함수 응용
- map : 함수라고 하는 타입이다.
정의 : 첫 번째 인자(input : 입력)로 함수를 받아서 두 번째 인자(input : 입력)인 반복 가능한 객체의 모든 요소에 적용
- map(int, 반복할 대상)
- ex) numbers = ['1', '2', '3']  
print(map(int, numbers))

### 세트(Set)
- 유일한 값을의 모음(collection)
- 순서가 없고 중복된 값이 없음
- 변경 가능, 반복 가능
    - 단, 순서가 없어 반복의 결과가 정의한 순서와 다를 수 있음

### 세트(Set) 생성
- 중괄호({}) 혹은 set()을 통해 생성
- 순서가 없어 별도의 값에 접근 불가능
```python
{1, 2, 3, 1, 2}
# {1, 2, 3} => 중복 값 제거
type({1, 2, 3})
# <class 'set'>
{'hi', 1, 2}
# {1, 2, 'hi'}
```

### 세트(set) 추가/삭제
- 값 추가 : .add()
- 값 삭제 : .remove()
```python
# 값 추가
num = {1, 2, 3}
num.add(5)
print(num)
# {1, 2, 3, 5}

num.add(1)
print(num)
# {1, 2, 3, 5}

# 값 삭제
num = {1, 2, 3}
num.remove(1)
print(num)
# {2, 3}

num = {1, 2, 3}
num.remove(5)
print(num)
# KeyError: 5
```

### 세트(set) 활용
- 세트를 활용하면 다른 컨테이너에서 중복된 값을 쉽게 제거 가능
    - 단, 이후의 순서가 무시되므로 순서가 중요한 경우 사용할 수 없음
```python
region = ['서울', '서울', '대전', '광주', '서울', '대전', '부산', '부산']
len(set(region))
# 4
set(region)
# {'광주', '대전', '부산', '서울'}
```