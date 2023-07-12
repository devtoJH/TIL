# console.log와 console.dir의 차이
    console.dir 및 console.log는 모두 브라우저의 개발자 콘솔에 정보를 인쇄하기 위해 JavaScript console 개체에서 제공하는 메서드. 그러나 그들은 다른 목적과 행동을 가지고 있다.

## console.dir
- 주로 JavaScript 객체의 속성과 메서드를 대화형 및 확장 가능한 방식으로 표시
- 속성을 트리 구조로 표시
- DOM 요소 또는 사용자 지정 JavaScript 개체와 같은 복잡한 개체를 탐색하고 해당 구조를 검사하는 데 특히 유용

## console.log
- 메시지, 변수 또는 기타 데이터를 콘솔에 출력하는 데 사용되는 범용 로깅 메소드
- 값을 문자열 표현으로 console에 출력
- 일반적으로 디버깅 목적으로 변수의 상태를 기록하거나 오류 메시지를 표시하거나 개발 중에 일반 정보를 제공하는 데 사용
- console.dir과 달리 console.log는 개체 속성 확장 및 축소와 같은 대화형 기능을 제공하지 않음

## 요약
- console.dir
    - 주로 대화형 방식으로 JavaSript 객체의 구조를 검사하는 데 사용

- console.log
    - 다양한 데이터 유형의 범용 로깅에 사용