# Float
    - 요소를 띄워서 텍스트 및 인라인 요소가 그 주위를 감싸도록 하는 배치
    - 띄워서 : 왼쪽 혹은 오른쪽으로 띄워 Normal Flow를 벗어남

## float 구문
```css
/* 키워드 값 */
float: left;
float: right;
float: none;
float: inline-start;
float: inline-end;

/* 전역 값 */
float: inherit;
float: initial;
float: unset;
```
- left : 요소가 자신의 포함 블록의 좌측에 부동(float)해야 함을 나타냄
- righy : 요소가 자신의 포함 블록의 우측에 부동(float)해야 함을 나타냄
- none : 요소가 부동하지 않아야 함을 나타냄
- inline-start : 요소가 자신의 포함 블록의 시작쪽에 부동해야 함을 나타냄
    - ltr(left to right) 스크립트 상에서 왼쪽
    - rtl(right to left) 스크립트 상에서 오른쪽
- inline-end : 요소가 자신의 포함 블록의 끝쪽에 부동해야 함을 나타냄
    - ltr(left to right) 스크립트 상에서 오른쪽
    - rtl(right to left) 스크립트 상에서 왼쪽

## float 형식 구문
```css
float = 
  block-start      |
  block-end        |
  inline-start     |
  inline-end       |
  snap-block       |
  <snap-block()>   |
  snap-inline      |
  <snap-inline()>  |
  left             |
  right            |
  top              |
  bottom           |
  none             |
  footnote         

<snap-block()> = 
  snap-block( <length> , [ start | end | near ]? )  

<snap-inline()> = 
  snap-inline( <length> , [ left | right | near ]? )
```