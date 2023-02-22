# CSS
    - Cascading Style Sheet
    - 웹 페이지의 디자인과 레이아웃을 구성하는 언어

```css
h1 {
    color: blue;
    font-size: 15px;
}
```
- h1 : 선택자(Selector)
- color: blue; : 선언(Declaration)
- font-size : 속성(Property)
- 15px : 값(Value)

## CSS 적용 방법
1. 인라인(Inline) 스타일
```html
<!DOCTYPE html>
<html lang="en">
<head>
    ...
</head>
<body>
    <h1 style="color: blue; background-color: yellow;">Hello World!</h1>
</body>
</html>
```

2. 내부(Internal) 스타일 시트
```html
<!DOCTYPE html>
<html lang="en">
<head>
<style>
    h1 {
        color: blue;
        background-color: yellow;
    }
</style>
</head>
<body>
    <h1>Hello World!</h1>
</body>
</html>
```

3. 외부(Extenal) 스타일 시트
- 별도의 CSS 파일 생성 후 불러오기
```html
<!DOCTYPE html>
<html lang="en">
<head>
    ...
    <link rel="styleesheet" href="style.css">
</head>
<body>
    <h1>Hello World!</h1>
</body>
</html>
```
```css
/* style.css */
h1 {
    color: blue;
    background-color: yellow;
}
```

## CSS Selectors
    HTML 요소를 선택하여 스타일을 적용할 수 있도록 함

## CSS Selectors 종류
- 기본 선택자
    - 전체(*) 선택자
    - 요소(tag) 선택자
    - 클래스(class) 선택자
    - 아이디(id) 선택자
    - 속성(attr) 선택자

- 결합자(Combinators)
    - 자손 결합자(" " (space))
    - 자식 결합자(>)

## CSS Selectors 특징
- 요소 선택자
    - 지정한 모든 태그를 선택

- 클래스 선택자
    - 주어진 클래스 속성을 가진 모든 요소를 선택
    - 예) .index는 class="index"를 가진 모든 요소를 선택

- 아이디 선택자
    - 주어진 아이디 속성을 가진 요소를 선택
    - 문서에는 주어진 아이디를 가진 요소가 하나만 있어야 함
    - 예) #index는 id="index"를 가진 요소를 선택

- 자손 선택자
    - 첫 번째 요소의 자손 요소들 선택
    - 예) p span은 p태그 안에 있는 모든 span태그를 선택(하위 레벨 상관 없이)

- 자식 선택자
    - 첫 번째 요소의 직계 자식만 선택
    - 예) ul > li은 ul태그 안에 있는 모든 li태그를 선택(한 단계 아래 자식들만)

### CSS Selectors 예시
```html
<body>
    <h1>Heading</h1>
    <h2>선택자 연습</h2>
    <h3>안녕?</h3>
    <h4 class="green">반가워요</h4>
    <p id="purple">과목 목록</p>
    <ul class="green">
        <li>파이썬</li>
        <li>알고</li>
        <li>웹
            <ol>
                <li>HTML</li>
                <li>CSS</li>
                <li>JS</li>
            </ol>
        </li>
    </ul>
    <p class="green">Lorem ipsum <span>dolor</span> sit amet consectetur adipisicing elit. Ab facere ipsa perferendis iure nemo, minus veniam mollitia voluptatibus fugit iste, quaerat, id ea. Nihil natus unde vel ipsum cupiditate dicta.</p>
</body>
</html>
```
```css
/* 전체 선택자 */
* {
     color: red;
}

/* 타입 선택자 */
h2 {
    color: skyblue;
}

h3, h4 {
        color: blue;
}

/* 클래스 선택자 */
.green {
    color: green;
}

/* 아이디 선택자 */
#purple {
    color: purple;
}

/* 자식 결합자 */
.green > span { /*클래스 green의 자식 태그 span에게 적용*/
    font-size: 50px;
}

/* 자손 결합자 */
.green li {
    color: orange;
}
```

# Cascade & Specificity
    동일한 요소에 적용 가능한 같은 스타일을 두 가지 이상 작성 했을 때 어떤 규칙이 이기는지 결정하는 것

## Cascade(계단식)
- 동일한 우선순위를 갖는 규칙이 적용될 때 CSS에서 마지막에 나오는 규칙이 사용
- 아래 예시에서 h1 태그 내용의 색은 blue가 적용됨
```css
h1 {
    color: red;
}

h1 {
    color: blue;
}
```

## Specificity(우선순위)
- 선택자 별로 정해진 우선순위 점수에 따라 점수가 높은 규칙이 사용
- 아래 예시에서 h1 태그 내용의 색은 red가 적용됨
```css
.make-red {
    color: red;
}

h1 {
    color: blue;
}
```

## 우선순위가 높은 순
1. Importance
    - !importance
    - **Cascade의 구조를 무시하고 모든 우선순위 점수 계산을 무효화하는 가장 높은 우선순위**

2. 우선 순위
    - 인라인 스타일 > id 선택자 > class 선택자 > 요소 선택자

3. 소스 코드 순서

## 상속
- 기본적으로 CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속함
- 이를 이용해 코드의 재사용성을 높임
- 상속 되는 속성
    - Text 관련 요소(font, color, text-align), opacity, visibility 등
- 상속 되지 않는 속성
    - Box model 관련 요소(width, height, margin, padding, border, box-sizing, display)
    - position 관련 요소(position, top/right/bottom/left, z-index) 등

---
## 참고
### CSS 인라인 스타일은 사용하지 말 것
- 문서 유지보수가 힘들어짐
- CSS와 HTML 구조 정보가 혼합되어 작성되기 때문에 코드를 이해하기 어렵게 만듦