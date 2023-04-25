# Ajax
- 비동기적인 웹 어플리케이션 개발을위한 프로그래밍 기술명
- **사용자의 요청에 대한 즉각적인 반응을 제공하면서, 페이지 전체를 다시 로드하지 않고 필요한 부분만 업데이트**

## 비동기(Asynchronous)
- 작업을 시작한 후 결과를 기다리지 않고 다음 작업을 처리하는 것 (병렬적 수행)
- 시간이 필요한 작업들은 요청을 보낸 뒤, 응답이 빨리 오는 작업부터 처리
- 예시
    - Gmail에서 메일 전송을 누르면 목록 화면으로 전환되지만 실제로 메일을 보내는 작업은 병렬적으로 뒤에서 처리됨
    ```javascript
    function slowRequest(callback) {
        console.log('1. 오래 걸리는 작업 시작')
        setTimeout(function () {
            callBack()
        }, 3000)
    }

    function myCallBack() {
        console.log('2. 콜백함수 실행')
    }

    slowRequest(myCallBack)
    console.log('3. 다른 작업 실행')

    // 출력 결과
    // 1. 오래 걸리는 작업 시작
    // 3. 다른 작업 실행
    // 2. 2. 콜백함수 실행
    ```

## 응답의 변화
- 기존
    - 사용자가 서버에게 HTTP request 보내고, 서버 측에선 사용자에게 HTML Document를 전송함

- Ajax
    - 사용자가 서버에게 XMLHttpRequest(XHR) 객체를 보내고, 서버 측에서도 사용자에게 XMLHttpRequest(XHR) 객체를 전송함

### XMLHttpRequest
- JavaScript 객체로, 클라이언트와 서버 간에 데이터를 비동기적으로 주고받을 수 있도록 해주는 객체
- **JavaScript 코드에서 서버에 요청을 보내고, 서버로부터 응답을 받을 수 있음**

## 비동기 요청

### Axios
- JavaScript에서 HTTP 요청을 보내는 라이브러리
- 주로 프론트엔드 프레임워크에서 사용

#### Axios 기본 문법
- get, post 등 여러 method 사용 가능
- then을 이용해서 성공하면 수행할 로직을 작성
- catch를 이용해서 실패하면 수행할 로직을 작성

```html
<script>
    axios({
        method: 'HTTP 메서드',
        url: `요청 URL`,
    })
        .then(성공하면 수행할 콜백함수)
        .catch(실패하면 수행할 콜백함수) 
</script>
```

## 'data-*' attributes
- 사용자 지정 데이터 특성을 만들어 임의의 데이터를 HTML과 DOM사이에서 교환할 수 있는 방법
- 예를 들어, data-test-value 라는 이름의 특성을 지정했다면 JavaScript에서는 element.dataset.testValue로 접근할 수 있음
- https://developer.mozilla.org/ko/docs/Web/HTML/Global_attributes/data-*

```html
<div data-my-id="my-data"></div>
<script>
   const myId = event.target.dataset.myId
</script>
```

---

<br>

## 참고

### 비동기를 사용하는 이유
#### "사용자 경험"
- 예를 들어 아주 큰 데이터를 불러온 뒤 실행되는 앱이 있을 때, 동기로 처리한다면 데이터를 모두 불러온 뒤에야 앱의 실행 로직이 수행되므로 사용자들은 마치 앱이 멈춘 것과 같은 경험을 겪게 됨
- 즉, 동기식 처리는 특정 로직이 실행되는 동안 다른 로직 실행을 차단하기 때문에 마치 프로그램이 응답하지 않는 듯한 사용자 경험을 만들게 됨
- 비동기로 처리한다면 먼저 처리되는 부분부터 보여줄 수 있으므로, 사용자 경험에 긍정적인 효과를 볼 수 있음
- 이와 같은 이유로 많은 웹 기능은 비동기 로직을 사용해서 구현되어 있음