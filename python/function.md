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

### 내장 함수
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