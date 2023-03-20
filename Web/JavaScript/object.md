# (plain)object
    키로 구분된 데이터 집합(data collection)을 저장하는 자료형

## 객체의 구조
- 중괄호를 이용해 작성
- 중괄호 안에는 key: value 쌍으로 구성된 속성(property)를 여러 개 넣을 수 있음
- key는 문자형, value는 모든 자료형이 허용

```javascript
const user = {
    name : 'Sophia',
    age : '30',
    'key with space' : true, // trailing comma : 속성을 추가, 삭제, 이동하기가 용이해짐
}
```

## 객체의 속성
1. property 활용
```javascript
// 조회
// 1. 점 표기법
console.log(user.age)
// 2. 대괄호 표기법
console.log(user['age'])
console.log(user['key with space'])

// 추가
user.address = 'korea'
console.log(user)

// 수정
user.age = 40
console.log(user)

// 삭제
delete user.address
console.log(user)
```

## property 존재 여부 확인 - 'in'
```javascript
// 속성 존재 여부 확인 (in)
console.log('age' in user)
console.log('country' in user)
```

## 단축 property
- 키 이름과 값으로 쓰이는 변수의 이름이 같은 경우 단축 구문을 사용할 수 있음
```javascript
// 단축 속성
const age = 30
const address = 'korea'

const oldUser = {
    age: age,
    address: address,
}

const newUser = {  // ES6에서 등장
    age,
    address,
}
```

## 계산된 property
- 키가 대괄호로 둘러싸여 있는 속성
- 고정된 값이 아닌 변수 값을 사용할 수 있음

```javascript
// 계산된 속성
const product = prompt('물건 이름을 입력해주세요.')
const a = 'my'
const b = 'property'

const bag = {
    [product]: 5,
    [a + b]: true,
}

console.log(bag)
```

# Method
    - 객체 속성에 정의된 함수
    - 'this'키워드를 사용해 객체에 대한 특정한 작업을 수행할 수 있음

## 메서드 예시
- object.method()
- 메서드는 객체를 '행동'할 수 있게 함

```javascript
const person = {
    name: 'Sophia',
    greeting: function () {
        return 'Hello'
    },
}

// greeting 메서드 호출
console.log(person.greeting()) // Hello
```

## 메서드 + this 예시
- object.method()
- 메서드는 객체를 '행동'할 수 있게 함

```javascript
const person = {
    name: 'Sophia',
    greeting: function () {
        return `Hello ${this.name}`
    },
}

// greeting 메서드 호출
console.log(person.greeting()) // Hello my name is Sophia
```

## 'this' keyword
    - 함수나 메서드를 호출한 객체를 가리키는 키워드
    - 함수 내에서 객체의 속성 및 메서드에 접근하기 위해 사용

- JS에서 this는 함수를 **호출하는 방법**에 따라 가리키는 대상이 다름
    1. 단순 호출 시 -> 전역 객체
    2. 메서드 호출 시 -> 메서드를 호출한 객체

- 단순 호출 시 this

```javascript
const myFunc = function () {
    return this
}

console.log(myFunc()) // window
```

- 메서드 호출 시 this

```javascript
const myObj = {
    data: 1,
    myFunc: function () {
        return this
    }
}

console.log(myObj.myFunc()) // myObj
```

## Nested 함수에서의 문제점과 해결책
- forEach의 인자로 들어간 함수는 일반 함수 호출이기 때무에 this가 전역 객체를 가리킴

```javascript
const myObj2 = {
    numbers: [1, 2, 3],
    myFunc: function () {
        this.numbers.forEach(function (number) {
            console.log(number) // 1 2 3
            console.log(this) // window
        })
    }
}
    console.log(myObj2.myFunc())
```

- **화살표 함수**는 자신만의 this를 가지지 않기 때문에 외부 함수에서 this 값을 가져옴

```javascript
const myObj3 = {
    numbers: [1, 2, 3],
    myFunc: function () {
        this.numbers.forEach((number) => {
            console.log(number) // 1 2 3
            console.log(this) // myObj3
        })
    }
}
    console.log(myObj2.myFunc())
```

---

# 참고
## 유용한 객체 메서드
```javascript
const profile = {
    name: 'Sophia',
    age: 30,
}

console.log(Object.keys(profile)) // ['name', 'age']
console.log(Object.values(profile)) // ['Sophia', 30]
```

## Javascript 'this' 특징
- Javascript에서 this는 함수가 '호출되는 방식'에 따라 결정되는 현재 객체를 나타냄
- Python의 self와 Java의 this는 선언 시 값이 이미 정해지는 것에 비해 Javascript의 this는 함수가 호출되기 전까지 값이 할당되지 않고 호출 시에 결정됨 (동적)

## JSON (Javascript Object Notation)
- key-value 형태로 이루어진 자료 표기법
- Javascript의 Object와 유사한 구조를 가지고 있지만 JSON은 형식이 있는 '문자열'
- Javascript에서 JSON을 사용하기 위해서는 Object 자료형으로 변경해야 함