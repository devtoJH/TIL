## 문자열(String)
    문자열은 immutable(변경 불가능한) 자료형이다.

### 문자열 슬라이싱
- s = 'abcdefghi'

(1) s[2:5] == 'cde'

|   | a | b | c | d | e | f | g | h | i |
|---|---|---|---|---|---|---|---|---|---|
| index | 0 | 1 | <span style="color:orange">2</span> | <span style="color:orange">3</span> | <span style="color:orange">4</span> | 5 | 6 | 7 | 8 |
| index | -9 | -8 | -7 | -6 | -5 | -4 | -3 | -2 | -1 |
---
(2) s[-6:-2] == 'defg'

|   | a | b | c | d | e | f | g | h | i |
|---|---|---|---|---|---|---|---|---|---|
| index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| index | -9 | -8 | -7 | <span style="color:orange">-6</span> | <span style="color:orange">-5</span> | <span style="color:orange">-4</span> | <span style="color:reoranged">-3</span> | -2 | -1 |
---
(3) s[2:5:2] == 'ce'
|   | a | b | c | d | e | f | g | h | i |
|---|---|---|---|---|---|---|---|---|---|
| index | 0 | 1 | <span style="color:orange">2</span> | <span style="color:skyblue">3</span> | <span style="color:orange">4</span> | 5 | 6 | 7 | 8 |
| index | -9 | -8 | -7 | -6 | -5 | -4 | -3 | -2 | -1 |
---
(4) s[-6:-1:3] == 'dg'
|   | a | b | c | d | e | f | g | h | i |
|---|---|---|---|---|---|---|---|---|---|
| index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| index | -9 | -8 | -7 | <span style="color:orange">-6</span> | <span style="color:skyblue">-5</span> | <span style="color:skyblue">-4</span> | <span style="color:orange">-3</span> | <span style="color:skyblue">-2</span> | -1 |
---
(5) s[2:5:-1] == ''
|   | a | b | c | d | e | f | g | h | i |
|---|---|---|---|---|---|---|---|---|---|
| index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| index | -9 | -8 | -7 | -6 | -5 | -4 | -3 | -2 | -1 |
---
(6) s[:3] == 'abc'
|   | a | b | c | d | e | f | g | h | i |
|---|---|---|---|---|---|---|---|---|---|
| index | <span style="color:orange">0</span> | <span style="color:orange">1</span> | <span style="color:orange">2</span> | 3 | 4 | 5 | 6 | 7 | 8 |
| index | -9 | -8 | -7 | -6 | -5 | -4 | -3 | -2 | -1 |
---
(7) s[5:] == 'fghi'
|   | a | b | c | d | e | f | g | h | i |
|---|---|---|---|---|---|---|---|---|---|
| index | 0 | 1 | 2 | 3 | 4 | <span style="color:orange">5</span> | <span style="color:orange">6</span> | <span style="color:orange">7</span> | <span style="color:orange">8</span> |
| index | -9 | -8 | -7 | -6 | -5 | -4 | -3 | -2 | -1 |
---
(8) s[:] == 'abcdefghi'
|   | a | b | c | d | e | f | g | h | i |
|---|---|---|---|---|---|---|---|---|---|
| index | <span style="color:orange">0</span> | <span style="color:orange">1</span> | <span style="color:orange">2</span> | <span style="color:orange">3</span> | <span style="color:orange">4</span> | <span style="color:orange">5</span> | <span style="color:orange">6</span> | <span style="color:orange">7</span> | <span style="color:orange">8</span> |
| index | -9 | -8 | -7 | -6 | -5 | -4 | -3 | -2 | -1 |
---
(9) s[::-1] == 'ihgfedcba'
|   | a | b | c | d | e | f | g | h | i |
|---|---|---|---|---|---|---|---|---|---|
| index | <span style="color:orange">0</span> | <span style="color:orange">1</span> | <span style="color:orange">2</span> | <span style="color:orange">3</span> | <span style="color:orange">4</span> | <span style="color:orange">5</span> | <span style="color:orange">6</span> | <span style="color:orange">7</span> | <span style="color:orange">8</span> |
| index | -9 | -8 | -7 | -6 | -5 | -4 | -3 | -2 | -1 |
---

### 문자열 메서드

(1) .split(기준 문자)
- 문자열을 일정 **기준**으로 나누어 **리스트로 반환**
- 괄호 안에 아무것도 넣지 않으면 자동으로 공백을 기준으로 설정
```python
word = 'I play the piano'
print(word.split())
# ['I', 'play', 'the', 'piano']
```
```python
word = 'apple,banana,orange'
print(word.split(','))
# ['apple', 'banana', 'orange']
```
```python
word = 'This_is_snake_case'
print(word.split('_'))
# ['This', 'is', 'snake', 'case']
```

(2) .strip(제거할 문자)
- 문자열의 **양쪽** 끝에 잇는 특정 문자를 모두 **제거**한 새로운 문자열 반환
- 괄호 안에 아무것도 넣지 않으면 자동으로 공백을 제거 문자로 설정
- 제거할 문자를 여러 개 넣으면 해당하는 모든 문자들을 제거
```python
word = ' Hello World '
print(word.strip())
# Hello World
```
```python
word = 'aHello Worlda'
print(word.strip('a'))
# Hello World
```
```python
word = 'Hello World'
print(word.strip('Hd'))
# ello Worl
```
```python
word = ' Hello Worldddddd'
print(word.strip('d'))
# Hello Worl
```

(3) .find(찾는 문자)
- 특정 문자가 처음으로 나타나는 **위치(인덱스)**를 반환
- 찾는 문자가 없다면 **-1**을 반환
```python
word = 'apple'
print(word.find('p'))
# 1
```
```python
word = 'apple'
print(word.find('k'))
# -1
```

(4) .index(찾는 문자)
- 특정 문자가 처음으로 나타나는 **위치(인덱스)**를 반환
- 찾는 문자가 없다면 **오류**발생
```python
word = 'apple'
print(word.index('p'))
# 1
```
```python
word = 'apple'
print(word.index('k'))
# ValueError : substring not ~
```

(5) .count(개수를 셀 문자)
- 문자열에서 특정 문자가 **몇 개**인지 반환
- 문자 뿐만 아니라, 문자열의 개수도 확인 가능
```python
word = 'banana'
print(word.count('a'))
# 3
```
```python
word = 'banana'
print(word.count('na'))
# 2
```
```python
word = 'banana'
print(word.count('nan'))
# 1
```

(6) .replace(기존 문자, 새로운 문자)
- 문자열에서 기존 문자를 새로운 문자로 **수정**한 새로운 문자열 반환
- 특정 문자를 빈 문자열("")로 수정하여 마치 해당 문자를 삭제한 것 같은 효과 가능
```python
word = 'happyhacking'
print(word.replace('happy', 'angry'))
# angryhacking
```
```python
word = 'happyhacking'
print(word.replace('h', 'H'))
# HappyHacking
```
```python
word = 'happyhacking'
print(word.replace('happy', ''))
# hacking
```

(7) 삽입할 문자.join(iterable)
- iterable의 **각각 원소 사이에 특정 문자를 삽입**한 새로운 문자열 반환
- 공백 출력, 콤마 출력 등 원하는 **출력** 형태를 위해 사용
```python
word = 'happy'
print(' '.join(word))
# h a p p y
```
```python
word = 'happy'
print(','.join(word))
# h,a,p,p,y
```
```python
word = ['abc', 'de.kr']
print('@'.join(word))
# abc@de.kr
```
```python
word = ['h', 'a', 'p', 'p', 'y']
print(''.join(word))
# happy
```

### 아스키(ASCII) 코드
    - 알파벳을 표현하는 대표 인코딩 방식
    - 각 문자를 표현하는 데 1byte(8bits) 사용
        - 1bit : 통신 에러 검출용
        - 7bit : 문자 정보 저장(총 128개)

(1) ord(문자) : **문자 -> 아스키코드**로 변환하는 내장 함수
```python
print(ord('A'))
# 65

print(ord('a'))
# 97
```

(2) chr(아스키코드) : **아스키코드 -> 문자**로 변환하는 내장 함수
```python
print(ord(65))
# A

print(ord(97))
# a
```