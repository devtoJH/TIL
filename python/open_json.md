# 파일 입출력
```python
open(file, mode='r', encoding='UTF8')
```
- file : 파일명
- mode : 텍스트 모드
- encoding : 인코딩 방식(일반적으로 utf-8 활용)  
![image](./image/file_mode.png)

## 파일 활용
- with 키워드 활용  
```python
with open(file, mode='r', encoding='UTF8') as f:
```
- with 키워드를 활용하지 않으면, f.close()를 반드시 호출하여 종료시켜야 함.

# JSON
    - JSON은 자바스크립트 객체 표기법으로 개발환경에서 많이 활용되는 데이터 양식으로 웹 어플리케이션에서 데이터를 전송할 때 일반적으로 사용함

    - 딕셔너리 + 리스트로 구성
    

## JSON 파일의 활용
- 객체(리스트, 딕셔너리 등)를 JSON으로 변환
```python
import json
with open('file json', mode='r', encoding='UTF8') as f:
    file = json.load(f) # json을 객체(리스트, 딕셔너리 등)으로 변환
```

# pprint
    - 임의의 파이썬 데이터 구조를 예쁘게 인쇄할 수 있는 기능을 제공