# event
    - 무언가 일어났다는 신호, 사건
    - 모든 DOM 요소는 이러한 신호를 만들어 냄

## event 종류
- 마우스, input, 키보드, 터치 등
- DOM 요소는 event를 받고 받은 event를 '처리(이벤트 핸들러(처리기))'할 수 있음

## event handler
- 이벤트가 발생했을 때 실행되는 함수
- 사용자의 행동에 어떻게 반응할지를 JS 코드로 표현한 것

## .addEventListener()
- 대표적인 이벤트 핸들러 중 하나
- 특정 이벤트를 DOM 요소가 수신할 때마다 콜백 함수를 호출
- EventTarget.addEventListener(type, handler)
    - EventTarget : DOM 요소
    - type
        - 특정 이벤트 이름 (ex. 'click')
        - https://developer.mozilla.org/en-US/docs/Web/Events

    - handler
        - 발생한 이벤트 객체를 수신하는 콜백 함수
        - 콜백 함수는 발생한 Event object를 유일한 매개변수로 받음

### 이벤트 핸들러 예시

```html
<body>
  <button id="btn">버튼</button>

  <script>
    // 1. 버튼 선택
    const btn = document.querySelector('#btn')
    console.log(btn)

    // 2. 버튼에 이벤트 핸들러를 부착
    btn.addEventListener('click', (event) => {
      // 이벤트 객체
      console.log(event)

      // 이벤트가 발생한 대상
      // console.log(this) // 화살표 함수에서는 window
      console.log(event.target)
    })
  </script>
</body>
```

# 이벤트 핸들러 활용
## click 이벤트
- 버튼을 클릭하면 숫자를 1씩 증가

```html
<body>
  <button id="btn">버튼</button>
  <p id="counter">0</p>

  <script>
    // 0. 초기값 할당 (0)
    let counterNumber = 0
    
    // 1. 버튼 요소 선택
    const btn = document.querySelector('#btn')
    
    // 2. 버튼에 이벤트 핸들러 부착 (클릭 이벤트)
    btn.addEventListener('click', () => {
      // 2.1 버튼에 클릭 이벤트가 발생할때마다 실행할 코드를 작성
      // 2.2 초기값 += 1
      counterNumber += 1

      // 2.3 p 요소를 선택
      const pTag = document.querySelector('#counter')

      // 2.4 p 요소의 컨텐츠를 1 증가한 초기값으로 설정
      pTag.textContent = counterNumber
    })
  </script>
</body>
```

## input 이벤트
- 사용자의 입력 값을 실시간으로 출력하기

```html
<body>
  <input type="text" id="text-input">
  <p></p>

  <script>
    // 1. input 요소 선택
    const inputTag = document.querySelector('#text-input')
    console.log(inputTag)

    // 2. p 요소 선택
    const pTag = document.querySelector('p')

    // 3. input 요소에 이벤트 핸들러 부착 (input 이벤트)
    inputTag.addEventListener('input', (event) => {
      // 3.1 작성하는 데이터가 어디에 누적되고 있는지 찾기
      // console.log(event)
      console.log(event.target.value)

      // 3.2 p요소의 컨텐츠에 작성하는 데이터를 추가
      pTag.textContent = event.target.value
    })
  </script>
</body>
```

## click & input 이벤트
- 사용자의 입력 값을 실시간으로 출력하기
- 버튼을 클릭하면 출력한 겂의 스타일을 변경하기

```html
<body>
  <h1></h1>
  <button id="btn">클릭</button>
  <input type="text" id="text-input">

  <script>
    // 인풋
    const inputTag = document.querySelector('#text-input')
    const h1Tag = document.querySelector('h1')

    inputTag.addEventListener('input', (event) => {
      h1Tag.textContent = event.target.value
    })

    // 버튼
    const btn = document.querySelector('#btn')

    btn.addEventListener('click', () => {
      // console.log(h1Tag.classList.value)
      // h1Tag.classList.add('blue')

      // 1. toggle 방법
      h1Tag.classList.toggle('blue')

      // 2. if 방법
      // if (h1Tag.classList.value) {
      //   h1Tag.classList.remove('blue')
      // } else {
      //   h1Tag.classList.add('blue')
      // }
    })
  </script>
</body>
```

## 이벤트 취소하기
- 텍스트를 복사하려고 하면 알림창을 띄우면서 복사를 중단하기

```html
<body>
  <h1>정말 중요한 내용</h1>

  <script>
    const h1Tag = document.querySelector('h1')

    h1Tag.addEventListener('copy', (event) => {
      console.log(event)
      event.preventDefault() // 현재 event의 기본 동작을 중단
      alert('복사 할 수 없습니다.')
    })
  </script>
</body>
```

## lodash
- 모듈성, 성능 및 추가 기능을 제공하는 Javascript 유틸리티 라이브러리
- array, object 등 자료구조를 다를 때 사용하는 유용하고 간편한 함수들을 제공
- https://lodash.com/