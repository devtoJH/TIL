# 딕셔너리(Dictionary)
    1. 키-값(key-value) 싸으로 이뤄진 모음(collection)
    - 키 : 불변 자료형만 가능(리스트, 딕셔러리 등은 불가능함)
    - 값 : 어떠한 형태든 관계 없음
    2. 키와 값은 :로 구분하고 개별 요소는 ,로 구분
    3. 변경 가능하며(mutable), 반복 가능함(iterable)
    - 딕셔너리는 반복하면 키가 반환됨

## 딕셔너리 생성
- 키와 값이 쌍으로 이뤄진 자료구조
    - key는 변경 불가능한 데어터만 활용 가능  
        - string, integer, float, boolean, tuple, range
    - value는 모든 값으로 설정 가능(리스트, 딕셔너리 등)

## 딕셔너리 접근
```python
dict_variable = {
    "name": "mango",
    "color": "yellow"
}

dict_variable["color"]
# "yellow"
```

## 딕셔너리 키-값 추가 및 변경
- 딕셔너리에 키와 값의 쌍을 추가할 수 있으며
- 이미 해당하는 키가 있다면 기존 값이 변경됨
```python
students = {'홍길동': '100', '김철수': '90'}
students['홍길동'] = 80
# {'홍길동' : 80, '김철수' : 90}
students['박명희'] = 95
# {'홍길동' : 80, '김철수' : 90, '박명희' : 95}
```

## 딕셔너리 키-값 삭제
- 키를 삭제하고자하면.pop()을 활용하여 삭제하고다 하는 키를 전달
```python
students = {'홍길동': '100', '김철수': '90'}
students.pop('홍길동')
students
# {'김철수' : 90}
```
- 키가 없는 경우는 keyError 발생
```python
students = {'홍길동': '100', '김철수': '90'}
students.pop('jane')
Traceback (most recent call last):
    File "<studin>", line 1, <module>
keyError: 'jane'
```

## 딕셔너리 순회
- 딕셔너리는 기본적으로 key를 순회라며, key를 통해 값을 활용
```python
grades = {'john': 80, 'eric': 90}
for name in grades:
    print(name)
# john
# eric
```
```python
grades = {'john': 80, 'eric': 90}
for name in grades:
    print(name, grades[name])
# john 80
# eric 90
```
- 추가 메서드를 활용하여 순회할 수 있음
    - keys() : key로 구성된 결과
    - values() : value로 구성된 결과
    - items() : (key, value)의 튜플로 구성된 결과
```python
grades = {'john': 80, 'eric': 90}
print(grades.keys())
print(grades.values())
print(grades.items())
# dict_keys(['john', 'eric'])
# dict_values([80, 90])
# dict_keys([('john', 80), ('eric', 90)])
```
```python
grades = {'john': 80, 'eric': 90}
for name, score in grades.items():
    print(name, score)
```