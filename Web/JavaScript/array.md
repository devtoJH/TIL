# Array
    순서가 있는 데이터 집합(data collection)을 저장하는 자료구조

## 배열의 구조
- 대괄호를 이용해 작성
- length를 사용해 배열에 담긴 요고가 몇 개인지 알 수 있음
- 배열 요소의 자료형엔 제약이 없음
- 배열의 마지막 요소는 객체와 마찬가지로 쉼표로 끝날 수 있음

```javascript
const fruits = ['apple', 'banana', 'coconut']

console.log(fruits[0])
console.log(fruits[1])
console.log(fruits[2])

console.log(fruits.length)

// 수정
fruits[1] = 'kiwi'
console.log(fruits) // ['apple', 'kiwi', 'coconut']
```

## 배열과 반복
```javascript
// 배열과 반복
// for
for (let i = 0; i < fruits.length; i++) {
  console.log(fruits[i])
}

// for...of
for (const fruit of fruits) {
  console.log(fruit)
}
```

## 배열과 메서드

| 메서드 | 기능 | 역할 |
|:---:|:---:|:---:|
| push / pop | 배열 끝 요소를 추가 또는 제거 | 요소 추가/제거 |
| unshift / shift | 배열 앞 요소를 추가 또는 제거 | 요소 추가/제거 |
| forEach | 인자로 주어진 함수(콜백 함수)를 배열 요소 각각에 대해 실행 | 반복 |
| map | 배열 요소 전체를 대성으로 함수(콜백 함수)를 호출하고, 함수 호출 결과를 배열로 반환 | 변형 |

### pop
- 배열 끝 요소를 제거하고, 제거한 요소를 반환

```javascript
const fruits = ['apple', 'banana', 'coconut']

// pop
console.log(fruits.pop()) // coconut
console.log(fruits) // ['apple', 'banana']
```

### push
- 배열 끝에 요소를 추가

```javascript
// push
fruits.push('orange')
console.log(fruits) // ['apple', 'banana', 'orange']
```

### shift
- 배열 앞 요소를 제거하고, 제거한 요소를 반환

```javascript
// shift
console.log(fruits.shift()) // apple
console.log(fruits) // ['banana', 'orange']
```

### unshift
- 배열 앞에 요소를 추가

```javascript
// unshift
fruits.unshift('melon')
console.log(fruits) // ['melon', 'banana', 'orange']
```

## forEach
- 인자로 주어진 함수(콜백 함수)를 배열 요소 각각에 대해 실행

## forEach 구조
```javascript
array.forEach(function (item, index, array) {
    // do something
})
```

- 콜백 함수는 3가지 매개변수로 구성
    1. item : 배열의 요소
    2. index : 배열 요소의 인덱스
    3. array :  배열

- 반환 값 : **undefined**

### forEach 예시
```javascript
const fruits = ['apple', 'banana', 'coconut']

fruits.forEach(function (item, index, array) {
    console.log(`${item} / ${index} / ${array}`)
})

fruits.forEach((item, index, array) => {
    console.log(`${item} / ${index} / ${array}`)
})
```

## 콜백 함수(Callback function)
- 다른 함수에 인자로 전달되는 함수
- 외부 함수 내에서 호출되어 일종의 루틴이나 특정 작업을 진행

## map
- 배열 요소 전체를 대상으로 함수(콜백 함수)를 호출하고, 함수 호출 결과를 모아 **새로운 배열을 반환**

## map 구조
- 기본적으로 forEach 동작 원리와 같지만 forEach와 달리 새로운 배열을 반환함

```javascript
const result = array.map(function (item, index, array) {
    // do something
})
```

### map 예시

```javascript
// 1
const fruits = ['apple', 'banana', 'coconut']

const result = fruits.map(function (fruit) {
  return fruit.length
})

const result2 = fruits.map((fruit) => {
  return fruit.length
})

console.log(result) // [5, 6, 7]

// 2
const numbers = [1, 2, 3]

const doubleNumber = numbers.map((number) => {
  return number * 2
})

console.log(doubleNumber) // [2, 4, 6]
```

## 배열 정리
- 배열의 본직은 객체
- 배열의 요소를 대괄호 접근법을 사용해 접근하는 건 객체 문법과 같음
- 다만 배열의 키는 숫자라는 점
- 숫자형 키를 사용함으로써 배열을 객체 기본 기능 이외에도 순서가 있는 컬렉션을 제어하게 해주는 특별한 메서드를 제공

---

# 참고
## 배열 순회 종합
- for loop
    - 배열의 인덱스를 이용하여 각 요소에 접근
    - break, continue 사용 가능

- for...of
    - 배열 요소에 바로 접근 가능
    - break, continue 사용 가능

- forEach (사용 권장)
    - 간결하고 가독성이 높음
    - callback 함수를 이용하여 각 요소를 조작하기 용이
    - break, continue 사용 불가능

```javascript
const chars = ['a', 'b', 'c', 'd']

// for loop
for (let idx = 0; idx < chars.length; idx++) {
  console.log(idx, chars[idx])
}

// for...of
for (const char of chars) {
  console.log(char)
}

// forEach
chars.forEach((char, idx) => {
  console.log(idx, char)
})
```

## 콜백 함수 구조를 사용하는 이유
- '함수의 재사용성 측면'
- 함수를 호출하는 코드에서 콜백 함수의 동작을 자유롭게 변경할 수 있음
- 예를 들어, map 함수는 콜백 함수를 인자로 받아 배열의 각 요소를 순회하며 콜백 함수를 실행
- 이때, 콜백 함수는 각 요소를 변환하는 로직을 담담하므로, map 함수를 호출하는 코드는 간결하고 가독성이 높아짐

<br>

- '비동기적 처리 측면'
- setTimeout 함수는 콜백 함수를 인자로 받아 일정 시간이 지난 후에 실행됨
- 이때, setTimeout 함수는 비동기적으로 콜백 함수를 실행하므로, 다른 코드의 실행을 방해하지 않음

```javascript
// 비동기 예시
console.log('a')

setTimeout(() => {
  console.log('b')
}, 3000) // 3000 -> 3초

console.log('c')

// a
// c
// b
```