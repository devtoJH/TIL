## 리스트(List)

### 배열 vs 연결 리스트
1. 배열 
    - **여러 데이터들이 연속된 메모리 공간에 저장되어 있는 자료 구조**
- 인덱스(index)를 통해 데이터에 빠르게 접근
- 배열의 길이는 변경 불가능 -> 길이를 변경하고 싶다면 새로 생성
- 데이터 타입 고정

2. 연결 리스트(Linked List)
    - **데이터가 담긴 여러 노드들이 순차적으로 연결된 형태의 자료 구조**
- 맨 처음 노드부터 순차적으로 탐색
- 연결 리스트의 길이 자유롭게 변경 가능 -> 삽입, 삭제가 편리
- 다양한 데이터 타입 저장
- 데이터가 메모리에 연속적으로 저장되지 않음

### 파이썬의 리스트
### 메서드
1. .append(원소) : 리스트 맨 끝에 새로운 원소 삽입
```python
a = [1, 2, 3, 4, 5]
a.append(6)
print(a)
# [1, 2, 3, 4, 5, 6]
```
```python
a = [1, 2, 3, 4, 5]
a.append(['a', 'b'])
print(a)
# [1, 2, 3, 4, 5, ['a', 'b']]
```
2. .pop(인덱스) : 특정 인덱스에 있는 원소를 삭제 및 반환
```python
a = [1, 2, 3, 4, 5]
b = a.pop()
print(a)
print(b)
# [1, 2, 3, 4]
# 5
```
```python
a = [1, 2, 3, 4, 5]
b = a.pop(2)
print(a)
print(b)
# [1, 2, 4, 5]
# 3
```
3. .count(원소) : 리스트에서 해당 원소의 개수를 반환
```python
a = [1, 2, 2, 3, 3, 3]
print(a.count(2))
# 2
```
```python
a = [1, 2, 2, 3, 3, 3]
print(a.count(3))
# 3
```
4. .index(원소) : 리스트에서 처음으로 원소가 등장하는 인덱스 반환
```python
a = [1, 2, 3, 2, 5]
print(a.index(2))
# 1
```
```python
a = [1, 2, 3, 2, 5]
print(a.index(8))
# ValueError : 8 is not in
```
5. .sort() : 리스트를 오름차순으로 정렬, reverse = True 옵션을 통해 내림차순으로 정렬 가능
```python
a = [5, 2, 4, 0, -1]
a.sort()
print(a)
# [-1, 0, 2, 4, 5]
```
```python
a = [5, 2, 4, 0, -1]
a.sort(reverse = True)
print(a)
# [5, 4, 2, 0, -1]
```
6. .reverse() : 리스트의 원소들의 **순서를 거꾸로 뒤집기**
```python
a = [1, 2, 3, 4, 5]
a.reverse()
print(a)
# [5, 4, 3, 2, 1]
```

### 내장 함수
1. len(iterable) : 리스트의 **길이**(원소의 개수)를 반환
```python
a = [1, 2, 3, 4, 5]
print(len(a))
# 5
```
2. sum(iterable) : 리스트의 모든 원소릐 **합**을 반환
```python
a = [1, 2, 3, 4, 5]
print(sum(a))
# 15
```
3. max(iterable) : 리스트의 원소 중 **최대값**을 반환
```python
a = [1, 2, 3, 4, 5]
print(max(a))
# 5
```
4. min(iterable) : 리스트의 원소 중 최소값을 반환
```python
a = [1, 2, 3, 4, 5]
print(min(a))
# 1
```
5. sorted(iterable) : 오름차순으로 **정렬**된 새로운 리스트 반환, 원본 리스트는 변화 없음
```python
a = [5, 2, -1, 0, 1]
b = sorted(a)
c = sorted(a, reverse=True)

print(a) # 원본
print(b) # 오름차순 정렬
print(c) # 내림차순 정렬
# [5, 2, -1, 0, 1]
# [-1, 0, 1, 2, 5]
# [5, 2, 1, 0, -1]
```
6. reverse(iterable) : 리스트의 순서를 거꾸로 **뒤집은** 새로운 객체 반환, 원본 리스트는 변화 없음
```python
a = [1, 2, 3, 4, 5]
b = reverse(a)
c = list(reverse(a))

print(a) # 원본
print(b) # reverse(a)
print(c) # 원본의 순서를 뒤집음
# [1, 2, 3, 4, 5]
# <list_reverseiterator ~>
# [5, 4, 3, 2, 1]
```

### 리스트 컴프리헨션(List Comprehension)
    리스트를 생성하는 간단한 방법
(1)
```python
numbers = []
for i in range(5):
    numbers.append(i)
print(numbers)
# [0, 1, 2, 3, 4]
```
(1-1)
```python
numbers = [i for i in range(5)]
print(numbers)
# [0, 1, 2, 3, 4]
```
(2)
```python
odd_numbers = [i for i in range(10) if i % 2 == 1]
print(odd_numbers)
# [1, 3, 5, 7, 9] => if문으로 필터링도 가능
```