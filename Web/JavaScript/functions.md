# Funcion
    참조 자료형에 속하며 모든 함수는 Function object

## 함수의 구조
- 함수의 이름
- 함수의 매개변수
- 함수의 body를 구성하는 statement

```javascript
function name ([param[, param, [..., param]]]) {
    statements
    return value // return이 없다면 undefined를 반환
}
```

## 함수의 정의
- 선언식(function declaration)

```javascript
function funcname () {
    statements
}
```
```javascript
// 함수 선언식 예시
function add (num1, num2) {
    return num1 + num2
}

add(2, 7) // 9
```

- 표현식(function expression)

```javascript
const funcname = function () {
    statements
}
```
```javascript
const sub = function (num1, num2) {
    return num1 - num2
}

sub(7, 2) // 5
```

### 함수 표현식 특징
- 함수 이름이 없는 '익명 함수'를 사용할 수 있음
- 선언식과 달리 표현식으로 정의한 함수는 호이스팅이 되지 않으므로 코드에서 나타나기 전에 먼저 사용할 수 없음

```javascript
// 함수 선언식

add(2, 7) // 9

function add (num1, num2) {
    return num1 + num2
}
```
```javascript
// 함수 표현식
sub(7, 2)
// ReferenceError: Cannot access 'sub' before initalization 

const sub = function (num1, num2) {
    return num1 - num2
}
```

### 선언식과 표현식

|  | 선언식 | 표현식 |
|:---:|:---:|:---:|
| 특징 | - 익명 함수 사용 불가능 | - 익명 함수 사용 가능 |
|  | - 호이스팅 있음 | - 호이스팅 없음 |
| 비고 |  | 사용 권장 |

## 기본 함수 매개변수
    값이 없거나 undefined가 전달될 경우 이름 붙은 매개변수를 기본값으로 초기화

```javascript
const greeting = function (name = 'Anonymous') {
    return `Hi ${name}`
}

greeting() // Hi Anonymous
```

### 매개변수와 인자의 개수 불일치
- 매개변수 개수 < 인자 개수

```javascript
const noArgs = function () {
    return 0
}
noArgs(1, 2, 3) // 0

const twoArgs = function (num1, num2) {
    return [num1, num2]
}

twoArgs(1, 2, 3) // [1, 2]
```

- 매개변수 개수 > 인자 개수

```javascript
const threeArgs = function (num1, num2, num3) {
    return [num1, num2, num3]
}

threeArgs() // [undefined, undefined, undefined]
threeArgs(1) // [1, undefined, undefined]
threeArgs(2, 3) // [2, 3, undefined]

// 나머지 매개변수 (가변 인자)
const myFunc = function (num1, num2, ...restArgs) {
    return [num1, num2, restArgs]
}

console.log(myFunc(1, 2, 3, 4, 5))
console.log(myFunc(1, 2))
```

### 나머지 매개변수
    무한한 수의 인자를 '배열'로 허용하여 가변 함수를 나타내는 방법

- 함수 정의에는 하나의 나머지 매개변수만 있을 수 있음
- 나머지 매개변수는 함수 정의에서 마지막 매개변수여야 함

```javascript
// 나머지 매개변수 (가변 인자)
const myFunc = function (num1, num2, ...restArgs) {
    return [num1, num2, restArgs]
}

myFunc(1, 2, 3, 4, 5) // [1, 2, [3, 4, 5]]
myFunc(1, 2) // [1, 2, []]
```

## 화살표 함수 표현식
    함수 표현식의 간결한 표현법


### 화살표 함수 표현식 작성 순서
1. function 키워드 제거 후 매개변수와 중괄호 사이에 화살표(=>) 작성
2. 함수의 매개변수가 하나 뿐이라면 매개변수의 `()` 제거 가능
3. 함수 본문의 표현식이 한 줄이라면 `{}`와 `return` 제거 가능

```javascript
const arrow1 = function (name) {
    return `hello, ${name}`
}

// 1. function 키워드 삭제 후 화살표 작성
const arrow2 = (name) => {
    return `hello, ${name}`
}

// 2. 인자가 1개일 경우에만 () 생략 가능
const arrow3 = name => { return `hello, ${name}`}

// 3. 함수 바디가 return을 포함한 표현식이 1개일 경우에 {} & return 삭제 가능
const arrow4 = name => `hello, ${name}`
```

---

# 참고
## 화살표 함수 표현식 응용

```javascript
// 1. 인자가 없다면 () or _로 표시 가능
const noArgs1 = () => 'No args'
const noArgs2 = _ => 'No args'

// 2-1. object를 return 한다면 return을 명시적으로 작성해야 함
const returnObject1 = () => { return {key : 'value'}}

// 2-2. return을 적지 않으려면 소괄호로 감싸야 함
const returnObject2 = () => ({key : 'value'})
```