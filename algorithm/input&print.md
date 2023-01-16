### 1. 입력 활용 예시(input)
```python
word = input()
>>> apple
# word -> 'apple'
```
```python
# 문자열 입력 받기
a = input()

# 한 개 숫자 입력 받기
b = int(input())

# 여러 개 숫자 입력 받기
d, e = map(int, input().split())
f, g, h = map(float, input().split())

map(int, ['1', '2', '3']) => 입력 받은 각각의 원소에 int적용 => 정수 1, 2, 3 을 반환
map(int, ['123']) => 입력 받은 각각의 원소에 int적용
=> 리스트 뿐만 아니라 문자열에도 적용 가능
=> 정수 1, 2, 3 을 반환
```
```python
a, b = map(int, input().split())
>>> 1 2

a, b = map(int, '1 2'.split())

a, b = map(int, ['1', '2'])

a, b = 1, 2
```

### 2. 출력 활용 예시(print)
```python
print('ap')
print('ple')
# ap
# ple
```
```python
a = 'ap'
b = 'ple'

print(a, b)
# ap ple
```
```python
a = 'ap'
b = 'ple'

print(a, end='@')
print(b)
# ap@ple

print(a, b, sep='\n')
# ap
# ple
```
```python
a, b, c = map(int, input().split())
>>> 1 2 3

print(a, b, c, end='&')
# 1 2 3& => 끝에 & 생성
```