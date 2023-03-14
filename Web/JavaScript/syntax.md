# 변수

## 식별자(변수명) 작성 규칙
- 반드시 문자, 달러($) 또는 밑줄(_)로 시작
- 대소문자를 구분하며, 클래스명 외에는 모두 소문자로 시작
- 예약어 사용 불가
    - for, if, function 등
- 카멜케이스 (camelCase)
    - 변수, 객체, 함수에 사용
- 파스칼케이스(PascalCase)
    - 클래스, 생성자에 사용
-  대문자 스네이크 케이스(SNAKE_CASE)
    - 상수(constants)에 사용
    - 상수 : 개발자의 의도와 상관없이 변경될 가능성이 없는 값

## 변수 키워드
### 1. let

- 블록 스코프를 갖는 지역 변수를 선언
- 재할당 가능, 재선언 불가능

```html
<script>
    let number = 10 // 1. 선언 및 초기값 할당
    number = 20 // 2. 재할당
</script>
```
```html
<script>
    let number = 10 // 1. 선언 및 초기값 할당
    let number = 20 // 2. 재선언 불가능
</script>
```

### 2. const

- 블록 스코프를 갖는 지역 변수를 선언
- 재할당 불가능, 재선언 불가능
- 선언 시, 반드시 초기값 설정 필요

```html
<script>
    const number = 10 // 1. 선언 및 초기값 할당
    number = 20 // 2. 재할당 불가능
</script>
```
```html
<script>
    const number = 10 // 1. 선언 및 초기값 할당
    const number = 20 // 2. 재선언 불가능
</script>
```
```html
<script>
    const number // const' declarations must be initialized
</script>
```

### 3. var

- 재할당 가능, 재선언 가능
- ES6 이전에 변수를 선언할 때 사용되던 키워드
- "호이스팅"되는 특성으로 인해 예기치 못한 문제 발생 가능
    - 따라서 ES6 이후부터는 var대신 const와 let을 사용하는 것을 권장
- 함수 스코프(function scope)를 가짐
- 변수 선언 시 var, const, let 키워드 중 하나를 사용하지 않으면 자동으로 var로 선언됨

## 변수 선언 키워드 정리

- 기본적으로 const 사용을 권장
- 재할당을 해야 하는 경우만 let을 사용

# 데이터 타입
1. 원시 자료형
2. 참조 자료형

## 1. 원시 자료형(Primitive type)

- 변수에 값이 직접 저장되는 자료형
- 불변, 값이 복사
- 키워드
    - Number, String, Boolean, undefined, unll

```html
<script>
    const bar = 'baz'
    console.log(bar) // baz

    bar.toUpperCase()
    console.log(bar) // baz
</script>
```
```html
<script>
    let a = 10
    let b = a
    b = 20
    console.log(a) // 10
    console.log(b) // 20
</script>
```

### Number
- 정수 또는 실수형 숫자를 표현하는 자료형

```html
<script>
    const a = 13
    const b = -5
    const c = 3.14 // float -> 숫자 표현
    const d = 2.993e8 // 2.998 * 10^8 = 299,800,000
    const e = Infinity
    const f = -Infinity
    const g = NaN // Not a Number를 나타내는 값
</script>
```

### String
- 문자 또는 문자열을 표현하는 자료형
- 곱셈, 나눗셈, 뺄셈은 안되지만 덧셈을 통해 문자열끼리 붙일 수 있음
- "Template Literal"을 사용하여 문자열 사이에 변수 삽입 가능

```html
<script>
    const firstName = 'Tony'
    const lastName = 'Stark'
    const fullName = firstName + lastName
</script>
```
```html
<script>
    const age = 10
    const message = '홍길동은 ${age}세 입니다.'
    console.log(message)
</script>
```

### null
- 변수의 값이 없음을 의도적으로 표현할 때 사용

```html
<script>
    const lastName = null
    console.log(lastName) // null
</script>
```

### undefined
- 변수 선언 이후 직접 값을 할당하지 않으면 자동으로 할당됨

```html
<script>
    const firstName
    console.log(firstName) // undefined
</script>
```

### null 과 undefined
- 동일한 역할을 하는 이 두 개의 키워드가 존재하는 이유는 단순한 **JavaScript의 설계 실수**
- null이 원시 자료형임에도 불구하고 object로 출력되는 이유는 JavaScript 설계 당시의 버그를 해결하지 못한 것
    - 이미 null 타입에 의존성을 띄고 있는 많은 프로그램들이 망가질 수 있기 때문(하위 호환 유지)

```html
<script>
    typeof null          // "object"
    typeof undefined     // "undfined"
</script>
```

### Boolean
- true 와 false
- 조건문 또는 반복문에서 boolean이 아닌 데이터 타입은 자동 형변환 규칙에 따라 true 또는 false로 변환됨

### ToBoolean Converdions (자동 형변환)

| 데이터 타입 | false | true |
|:---:|:---:|:---:|
| undefined | 항상 false | X |
| null | 항상 false | X |
| Number | 0, -0, NaN | 나머지 모든 경우 |
| String | 빈 문자열 | 나머지 모든 경우 |

## 2. 참조 자료형(Reference type)

- 객체의 주소가 저장되는 자료형
- 가변, 주소가 복사
- 키워드
    - Objects(Object, Array, Function)

# 연산자

## 할당 연산자
- 오른쪽에 있는 피연산자의 평가 결과를 왼쪽 피연산자에 할당하는 연산자
- 다양한 연산에 대한 단축 연산자 지원
- Increment(++)
    - 피연산자의 값을 1 증가시키는 연산자
- Decrement(--)
    - 피연산자의 값은 1 감소시키는 연산자
- += 또는 -=와 같이 더 분명한 표현으로 적을 것을 권장

```html
<script>
    let c = 0

    c += 10
    console.log(c) // 10

    c -= 3
    console.log(c) // 7

    c *= 10
    console.log(c) // 70

    c++
    console.log(c) // 71

    c--
    console.log(c) // 70
</script>
```

## 비교 연산자
- 피연산자들(숫자, 문자, Boolean 등)을 비교하고 결과값을 boolean으로 반환하는 연산자

```html
<script>
    3 > 2 // true
    3 < 2 // false

    'A' < 'B' // true
    'Z' < 'a' // true
    '가' < '나' // true
</script>
```

## 동등 연산자
- 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환
- 비교할 때 안묵적 타입 변환 통해 타입을 일치시킨 후 같은 값인지 비교
- 두 피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별
- **예상치 못한 결과가 발생할 수 있으므로 특별한 경우를 제외하고 사용하지 않음**

```html
<script>
    const a = 1
    const b = '1'
    console.log(a == b) // true
    console.log(a == true) // true

    // 자동 형변환 예시
    console.log(8 * null) // 0, null은 0
    console.log('5' - 1) // 4
    console.log('5' + 1) // '51'
    console.log('five' * 2) // NaN
</script>
```

## 일치 연산자
- 두 피연산자의 값과 타입이 모두 같은 경우 true를 반환
- 같은 객체를 가리키거나, 같은 타입이면서 같은 값인지를 비교
- 엄격한 비교가 이뤄지며 암묵적 타입 변환이 발생하지 않음

```html
<script>
    const a = 1
    const b = '1'

    console.log(a === b) // false
    console.log(a === Number(b)) // true
</script>
```

## 논리 연산자
- and => &&
- or => ||
- not => !
- 단축 평가 지원
    - ex) false && true => false
    - ex) false || true => true

```html
<script>
    true && false // false
    true && true // true

    false || true // true
    false || false // false

    !true // false

    1 && 0 // 0
    0 && 1 // 0
    4 && 7 // 0
    1 || 0 // 1
    0 || 1 // 1
    4 || 7 // 4
</script>
```

# 조건문

## if
- 조건 표현식의 결과값을 boolean 타입으로 변환 후 참/거짓을 판단

```html
<script>
   if (조건문) {
    명령문
   } else if (조건문) {
    명령문
   } else {
    명령문
   }
</script>
```
```html
<script>
    const name = 'manager'

    if (name === 'admin') {
        console.log('관리자님 환영해요')
    } else if (name === 'manager') {
        console.log('매니저님 환영해요')
    } else {
        console.log(`반갑습니다. ${name}님`)
    }
</script>
```

# 반복문

## 반복문 종류
- while
- for
- for...in
- for...of

### while
- 조건문이 참이기만 하면 문장을 계속해서 수행

```html
<script>
    while (조건문) {
        // do something
    }
</script>
```
```html
<script>
    let i = 0

    while (i < 6) {
        console.log(i)
        i += 1
    }
</script>
```

### for
- 특정한 조건이 거짓으로 판별될 때까지 반복
- 변수 선언할 때, let만 사용 가능
    - 변수를 재할당하기 때문에 const를 사용하면 에러 발생

```html
<script>
    for ([초기문]; [조건문]; [증감문]) {
        // do something
    }
</script>
```
```html
<script>
    for (let i = 0; i < 6; i++) {
        console.log(i)
    }
</script>
```

- for 동작 원리

```html
<script>
    for (let i = 0; i < 6; i++) {
        console.log(i) // 0, 1, 2, 3, 4, 5
    }
</script>
```
```html
<script>
    // 1. 반복문 진입 및 변수 i 선언
    for (let i = 0; ...; ...) {
        ...
    }
</script>
```
```html
<script>
    // 2. 조건문 평가 후 코드 블럭 실행
    for (...; i < 6; ...) {
        console.log(i)
    }
</script>
```
```html
<script>
    // 3. 코드 블록 실행 이후 i 값 증가
    for (...; ...; i++) {
        ...
    }
</script>
```
- 조건문이 성립할 때까지 2, 3번 반복 실행

### for...in
- 객체(object)의 속성을 순회할 때 사용
- let, const 사용 가능
    - 재할당 개념이 아니기 때문에 둘 다 사용 가능
- **배열도 순회 가능하지만 인덱스 순으로 순회한다는 보장이 없으므로 권장하지 않음**

```html
<script>
    for (variable in object) {
        statements
    }
</script>
```
```html
<script>
    const fruits = {
        a: 'apple',
        b: 'banana'
    }
    
    for (const key in fruits) {
        console.log(key) // a, b
        console.log(fruits[key]) // apple, banana
    }

</script>
```

### for...of
- 반복 가능한 객체(배열, 문자열 등)를 순회할 때 사용
- let, const 사용 가능

```html
<script>
    for (variable of object) {
        statements
    }
</script>
```
```html
<script>
    const numbers = [0, 1, 2, 3]

    for (const number of numbers) {
        console.log(number) // 0, 1, 2, 3
    }

    const myStr = 'apple'

    for (const str of myStr) {
        console.log(str) // a, p, p, l, e
    }
</script>
```

### for...in 과 for...of의 차이점
- for...in : "속성 이름"을 통해 반복
- for...of : "속성 값"을 통해 반복

```html
<script>
    const arr = [3, 5, 7]

    for (const i in arr) {
        console.log(i) // 0, 1, 2 => 인덱스 값
    }

    for (const i of arr) {
        console.log(i) // 3, 5, 7 => 속성 값
    }
</script>
```

## 반복문 정리

| 키워드 | 연관 키워드 | 스코프 |
|:---:|:---:|:---:|
| while | break, continue | 블록 스코프 |
| null | break, continue | 블록 스코프 |
| Number | object 순회 | 블록 스코프 |
| String | iterable 순회 | 블록 스코프 |

<br>

# 참고

## 세미콜론(semicolon)
- 자바스크립트는 세미콜론을 선택적으로 사용 가능
- 세미콜론이 없으면 ASI에 의해 자동으로 세미콜론이 삽입됨
    - ASI (Automatic Semicolon Insertion, 자동 세미콜론 삽입 규칙)

## 블록 스코프
- if, for, 함수 등의 **중괄호({}) 내부**를 가리킴
- 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능

```html
<script>
    let x = 1

    if (x === 1) {
        let x = 2
        console.log(x) // 2
    }

    console.log(x) // 1
</script>
```

## 함수 스코프
- 함수의 중괄호 내부를 가리킴
- 함수 스코프를 가지는 변수는 함수 바깥에서 접근 불가능

```html
<script>
    function foo() {
        var x = 5
        oconsole.log(x) // 5
    }

    // ReferenceError: x is not defined
    console.log(x)
</script>
```

## 호이스팅(hoisting)
- 변수를 선언 이전에 참조할 수 있는 현상
- var로 선언된 변수는 선언 이전에 참조할 수 있음
- 변수 선언 이전의 위치에서 접근 시 undefined를 반환

```html
<script>
    console.log(name) // undefined => 선언 이전에 참조

    var name = '홍길동' // 선언
</script>
```
```html
<script>
    // 위 코드를 암묵적으노 아래와 같이 이해함
    var name // undefined로 초기화
    console.log(name)

    var name = '홍길동'
</script>
```

- 즉, JavaScript에서 변수들은 실제 실행 시에 코드의 최상단으로 끌어 올려지게 되며(hoisted) 이러한 이유 때문에 var로 선언된 변수는 선언 시에 undefined로 값이 초기화되는 과정이 동시에 일어남
- 반면 let, const는 호이스팅이 일어나면 에러를 발생시킴

```html
<script>
    console.log(username) // undefined
    var username = '홍길동'

    console.log(email) // Uncaught ReferenceError
    let email = 'gildong@mail.com'

    console.log(age) // Uncaught ReferenceError
    const age = 50
</script>
```

## 템플릿 리터럴(Template literals)
- 내장된 표현식을 허용하는 문자열 작성 방식
-  ES6+ 부터 지원
- Backtick(``)을 이용하며, 여러 줄에 걸쳐 문자열을 정의할 수도 있고 JavaScript의 변수를 문자열 안에 바로 열결할 수 있는 이점이 생김
- 표현식은 $와 중괄호(${expression})로 표기

```html
<script>
    const age = 10
    const mesasge = `홍길동은 ${age}세 입니다.`
</script>
```

## NaN을 반환하는 경우
1. 숫자로서 읽을 수 없음(Number(undefined))
2. 결과가 허수인 수학 계산식 (Math.sqrt(-1))
3. 피연산자가 NaN (7 ** NaN)
4. 정의할 수 없는 계산식 (0 * infinity)
5. 문자열을 포함하면서 덧셈이 아닌 계산식 ('가' / 3)