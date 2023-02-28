# Flexbox
    - 요소를 행과 열 형태로 배치하는 1차원 레이아웃 방식
    - 요소간 '공간 배열'과 '정렬'

## Flexbox 기본 사항
![](./image/flexbox.png)

## Flexbox 용어
- main axis (주축)
    - flex item들이 배치되는 기본 축
    - main start에서 시작하여 main end 방향을 배치

- cross axis (교차 축)
    - main axis에 수직인 축
    - cross start에서 시작하여 cross end 방향으로 배치

- flex container
    - display: flex; 혹은 display: inline-flex;가 설정된 부모 요소
    - 이 컨테이너의 1차 자식 요소들이 flex item이 됨
    - flexbox 속성 값들을 사용하여 자식 요소 flex item들을 배치

- flex item
    - flex container 내부에 레이아웃 되는 항목

## Flexbox 속성
- flex container 관련 속성
    - display, flex-direction, flex-wrap, justify-content, align-items, align-content

- flex item 관련 속성
    - oalign-self, flex-grow, flex-shrink, flex-basis, order


## Flexbox 속성 용어
1. flex container 지정
```css
.contanier {
    height: 500px;
    border: 1px solid black;
    display: flex;
}
```
- flex item은 행으로 나열
- flex item은 주축의 시작 선에서 시작
- flex item은 교차축의 크기를 채우기 위해 늘어남

2. flex-direction 지정
```css
.contanier {
    /* 수평(좌 -> 우) */
    flex-direction: row;
    /* 수직(상 -> 하) */
    flex-direction: column;
    /* 수평(우 -> 좌) */
    flex-direction: row-reverse;
    /* 수직(하 -> 상) */
    flex-direction: column-reverse;
}
```
- flex item이 나열되는 방향을 지정
- column으로 지정할 경우 주 축이 변경됨(row -> column)
- -reverse로 지정하면 시작 선과 끝 선이 서로 바뀜

3. flex-wrap
```css
.contanier {
    flex-wrap: wrap;
    flex-wrap: nowrap;
}
```
- flex item 목록이 flex container의 하나의 행에 들어가지 않을 경우 다른 행에 배치할지 여부 설정

4. justify-content
```css
.contanier {
    /* 좌측 정렬 */
    justify-content: flex-start;
    /* 가운데 정렬 */
    justify-content: center;
    /* 우측 정렬 */
    justify-content: flex-end;
}
```
- 주 축을 따라 flex item과 주위에 공간을 분배

5. align-content
```css
.contanier {
    flex-wrap: wrap;
    /* 상단 정렬 */
    align-content: flex-start;
    /* 가운데 정렬 */
    align-content: center;
    /* 하단 정렬 */
    align-content: flex-end;
}
```
- 교차 축을 따라 flex item과 주위에 공간을 분배
- flex-wrap이 wrap 또는 wrap-reverse로 설정된 여러 행에만 적용됨
- 한 줄 짜리 행에는 (flex-wrap이 nowrap으로 설정된 경우) 효과 없음

6. align-items
```css
.contanier {
    flex-wrap: wrap;
    /* 상단 정렬 */
    align-items: flex-start;
    /* 가운데 정렬 */
    align-items: center;
    /* 하단 정렬 */
    align-items: flex-end;
}
```
- 교차 축을 따라 flex item 행을 정렬

7. align-self
```css
.item1 {
    align-self: center;
}

.item2 {
    align-self: flex-end;
}
```
- 교차 축을 따라 개별 flex item을 정렬

8. flex-grow
```css
.container {
      width: 100%;
      display: flex;
}

.item {
  height: 100px;
  color: white;
  font-size: 3rem;
}

.item-1 {
  background-color: red;
  flex-grow: 1;
}

.item-2 {
  background-color: green;
  flex-grow: 2;
}

.item-3 {
  background-color: blue;
  flex-grow: 3;
}
```
```html
<div class="container">
    <div class="item item-1">1</div>
    <div class="item item-2">2</div>
    <div class="item item-3">3</div>
</div>
```
- 남는 행 여백을 비율에 따라 각 flex item에 분배
- flex-grow의 반대는 flex-shrink
    - 넘치는 너비를 분배해서 줄임

9. flex-basis
```css
.container {
      width: 100%;
      display: flex;
    }

.item {
    height: 100px;
    color: white;
    font-size: 3rem;
}

.item-1 {
    background-color: red;
    flex-basis: 300px;
}

.item-2 {
    background-color: green;
    flex-basis: 600px;
}

.item-3 {
    background-color: blue;
    flex-basis: 300px;
}
```
```html
<div class="container">
    <div class="item item-1">1</div>
    <div class="item item-2">2</div>
    <div class="item item-3">3</div>
</div>
```
- flex item의 초기 크기 값을 지정
- flex-basis와 width 값을 동시에 적용한 경우 flex-basis이 우선

## 목적에 따른 분류
- 배치 설정
    - flex-direction
    - flex-wrap

- 공간 분배
    - justify-content
    - align-content

- 정렬
    - align-items
    - align-self

### 속성명 tip
- justify : 주축
- align : 교차축