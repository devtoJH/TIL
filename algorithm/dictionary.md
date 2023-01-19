## 딕셔너리(dictionary)
    해시 함수와 해시 테이블을 이용하기 때문에
    삽입, 삭제, 수정, 조회 연산의 속도가 리스트보다 빠르다.

### 해시 테이블
- 해시 함수 : 임의 길이의 데이터를 고정 길이의 데이터로 매핑하는 함수
- 해시 : 해시 함수를 통해 얻어진 값

### 딕셔너리 연산의 시간 복잡도
| 연산 종류 | 시간 복잡도 |
|:---:|:---:|
| Get Item | O(1) |
| Insert Item | O(1) |
| Update Item | O(1) |
| Delete Item | O(1) |
| Search Item | O(1) |

### 딕셔너리 기본 문법
1. 선언
- **변수 = {key1:value1, key2:value2}**
```python
a = {
    'name' : 'kyle',
    'gender' : 'male',
    'address' : 'seoul'
}
print(a)
# {'name' : 'kyle', 'gender' : 'male', 'address' : 'seoul'}
```

2. 삽입 및 수정
- **딕셔너리[key] = value**
- 내부에 해당 key가 없으면 삽입, 있으면 수정
```python
# 삽입
a = {
    'name' : 'kyle',
    'gender' : 'male',
    'address' : 'seoul'
}
a['job'] = 'coach'
print(a)
# {'name' : 'kyle', 'gender' : 'male', 'address' : 'seoul', 'job' : 'coach'}


# 수정
a = {
    'name' : 'kyle',
    'gender' : 'male',
    'address' : 'seoul'
}
a['name'] = 'justin'
print(a)
# {'name' : 'justin', 'gender' : 'male', 'address' : 'seoul', 'job' : 'coach'}
```

3. 삭제(1)
- **딕셔너리.pop(key)**
- 내부에 존재하는 key에 대한 value 삭제 및 반환, 존재하지 않는 key에 대해서는 KeyError 발생
```python
a = {
    'name' : 'kyle',
    'gender' : 'male',
    'address' : 'seoul'
}
gender = a.pop('gender')
print(a)
print(gender)
# {'name' : 'kyle', 'address' : 'seoul'}
# male


a = {
    'name' : 'kyle',
    'gender' : 'male',
    'address' : 'seoul'
}
phone = a.pop('phone')
print(a)
print(phone)
# KeyError
```

3. 삭제(2)
- **딕셔너리.pop(key, value)**
- 두 번째 인자로 default(기본)값을 지정하여 KeyError 방지 가능
```python
a = {
    'name' : 'kyle',
    'gender' : 'male',
    'address' : 'seoul'
}
gender = a.pop('phone', '010-1234-5678')
print(a)
print(phone)
# {'name' : 'kyle', 'gender' : 'male', 'address' : 'seoul'}
# 010-1234-5678
```

4. 조회
- **딕셔너리[key], 딕셔너리.get(key, value)**
- key에 해당하는 value 반환
```python
a = {
    'name' : 'kyle',
    'gender' : 'male',
    'address' : 'seoul'
}
# 1
print(a['name'])
# kyle


a = {
    'name' : 'kyle',
    'gender' : 'male',
    'address' : 'seoul'
}
# 2
print(a.get('name'))
# kyle
```

4. 조회(딕셔너리[key], 딕셔너리.get(key, value))
```python
# 딕셔너리[key]
a = {
    'name' : 'kyle',
    'gender' : 'male',
    'address' : 'seoul'
}
# 1
print(a['phone'])
# KeyError


# 딕셔너리.get(key, value)
a = {
    'name' : 'kyle',
    'gender' : 'male',
    'address' : 'seoul'
}
# 1
print(a.get('phone'))
# None

a = {
    'name' : 'kyle',
    'gender' : 'male',
    'address' : 'seoul'
}
# 1
print(a.get('phone', '없음'))
# 없음
```

### 딕셔너리 메서드
(1) .keys() : 딕셔너리의 **key 목록**이 담긴 dict_keys 객체 반환
```python
a = {
    'name' : 'kyle',
    'gender' : 'male',
    'address' : 'seoul'
}
print(a.keys())
# dict_keys(['name', 'gender', 'address'])

a = {
    'name' : 'kyle',
    'gender' : 'male',
    'address' : 'seoul'
}
for key in a.keys():
    print(key)
# name
# gender
# address

a = {
    'name' : 'kyle',
    'gender' : 'male',
    'address' : 'seoul'
}
for key in a:
    print(key)
# name
# gender
# address
```

(2) .values() : 딕셔너리의 **value 목록**이 담긴 dict_values 객체 반환
```python
a = {
    'name' : 'kyle',
    'gender' : 'male',
    'address' : 'seoul'
}
print(a.values())
# dict_keys(['kyle', 'male', 'seoul'])

a = {
    'name' : 'kyle',
    'gender' : 'male',
    'address' : 'seoul'
}
for value in a.values():
    print(value)
# kyle
# male
# seoul
```

(3) .items() : 딕셔너리의 **(key, value) 쌍 목록**이 담긴 dict_items 객체 반환
```python
a = {
    'name' : 'kyle',
    'gender' : 'male',
    'address' : 'seoul'
}
print(a.items())
# dict_items([('name', 'kyle'), ('gender', 'male'), ('address', 'seoul')])

a = {
    'name' : 'kyle',
    'gender' : 'male',
    'address' : 'seoul'
}
for item in a.items():
    print(item)
# ('name', 'kyle')
# ('gender', 'male')
# ('address', 'seoul')

a = {
    'name' : 'kyle',
    'gender' : 'male',
    'address' : 'seoul'
}
for key, value in a.items():
    print(key, value)
# name kyle
# gender male
# address seoul
```