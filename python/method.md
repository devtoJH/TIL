# 메서드
    클래스의 행위를 표현하는 것으로 클래스 내의 함수로 볼 수 있다.

## 메서드 기본 구조
```python
object.method_name()
```

### 문자열
- 문자들의 나열(sequence of characters)
    - 모든 문자는 str타입
- 문자열은 작은 따옴표(')나 큰 따옴표(")를 활용하여 표기

### 문자열 탐색
- s.find(x) : x의 첫 번째 위치를 반환. 없으면 -1을 반환
```python
print('apple'.find('p'))
# 1
print('apple'.find('k'))
# -1
```
- s.index(x) : x의 첫 번째 위치를 반환. 없으면 오류 발생
```python
print('apple'.index('p'))
# 1
print('apple'.index('k'))
# ValueError : substring not found
```

### 문자열 검증
- s.isalpha() : 알파벳 문자 여부
- s.isupper() : 대문자 여부
- s.islower() : 소문자 여부
- s.istitile() : 타이틀 형식 여부

### 문자열 변경
1. .replace(old, new[,count])
    - 바꿀 대상 글자를 새로운 글자로 바꿔서 반환
    - count를 지정하면, 해당 개수만큼만 시행
```python
print('coone'.replace('o', 'a'))
# caane
print('wooooowoo'.replace('o', '!', 2))
# w!!ooowoo
```
2. .strip([chars])
    - 특정한 문자들을 지정하면,
    - 양쪽을 제거하거나(strip), 왼쪽을 제거하거나(lstrip), 오른쪽을 제거(rstrip)
    - 문자열을 지정하지 않으면 공백을 제거함
```python
print('    와우!\n'.strip())
# '와우!'
print('    와우!\n'.lstrip())
# '와우!\n'
print('    와우!\n'.rstrip())
# '    와우!'
print('안녕하세요????'.strip('?'))
# '안녕하세요'
```
3. .split(sep = None, maxsplit = -1)
    - 문자열을 특정한 단위로 나눠 리스트로 반환
    - sep이 None이거나 지정되지 않으면 연속된 공백문자를 단일한 공백문자로 간주하고, 선행/후행 공백은 빈 문자열에 포함시키지 않음
    - maxsplit이 -1인 경우에는 제한이 없음
```python
print('a,b,c'.split('_'))
# ['a,b,c']
print('a b c'.split())
# ['a', 'b', 'c']
```
4. 'separator'.join([iterable])
    - 반복가능한(iterable) 컨테이너 요소들을 구분자(separator)로 합쳐 문자열 반환
    - iterable에 문자열이 아닌 값이 있으면 TypeError 발생
```python
print(''.join(['3', '5']))
# 35
```

### 리스트(list)
    - 변경 가능한 값들의 나열된 자료형
    - 순서를 가짐, 서로 다른 타입의 요소를 가질 수 있음
    - 변경 가능, 반복 가능
    - 항상 대괄호로 구성, 요소는 콤마로 구분
    - [1, 2, 3, 4, 5]

### 값 추가
- .append(x) : 리스트에 값을 추가함
- .extend(iterable) : 리스트에 iterable의 항목을 추가함
- .insert(i, x) : 정해진 위치 i에 x값을 추가함
### 값 삭제
- .remove(x) : 리스트에서 값이 x인 것을 삭제
    - 값이 없는 경우 : ValueError 발생
- .pop(i)
    - 정해진 위치에 i에 있는 값을 삭제하고, 그 항목을 반환함
    - i가 지정되지 않으면, 마지막 항목을 삭제하고 반환함
- .clear() : 모든 항목을 삭제함

### 탐색/정렬
- .index(x) : x값을 찾아 해당 index 값을 반환
- .count(x) : 원하는 값의 개수를 반환
- .sort()
    - 원본 리스트를 정렬, None 반환
    - sorted 함수와 비교할 것
    ```python
    # .sort()
    num = [3, 2, 5, 1]
    result = num.sort()
    print(num, result)
    # [1, 2, 3, 5] None => 원본 변경

    # sorted()
    num = [3, 2, 5, 1]
    result = sorted(num)
    print(num, result)
    # [3, 2, 5, 1] [1, 2, 3, 5] => 정렬된 리스트를 반환, 원본 변경 없음
    ```
- .reverse() : 순서를 반대로 뒤집음(정렬하는 것이 아님), None 반환
    ```python
    # .sort()
    num = [3, 2, 5, 1]
    result = num.reverse()
    print(num, result)
    # [1, 5, 2, 3] None
    ```
### 세트(set)
- 유일한 값을의 모음(collection)
- 순서가 없고 중복된 값이 없음
- 변경 가능, 반복 가능
    - 단, 순서가 없어 반복의 결과가 정의한 순서와 다를 수 있음

### 딕셔너리(dictionary)
- 키-값 쌍으로 이뤄진 모음
    - 키(key) : 불변 자료형만 가능(리스트, 딕셔너리 등은 불가능)
    - 값(value) : 어떠한 형태든 관계 없음
- 변경 가능, 반복 가능
### 딕셔너리 조회
- .get(key[,default])
    - key를 통해 value를 가져옴
    - KeyError가 발생하지 않으며, default 값을 설정할 수 있음(기본 : None)
### 딕셔너리 삭제
- pop(key[,default])
    - key가 딕셔너리에 있으면 제거하고 해당 값을 반환
    - 그렇지 않으면 default를 반환
    - default값이 없으면 KeyError
### 딕셔너리 추가
- .update([other]) : 값을 제공하는 key, value로 덮어씀