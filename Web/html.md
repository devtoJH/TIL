# HTML
    - HyperText Markup Language
    - 웹 페이지의 의미와 구조를 정의하는 언어

## HyperText
- 웹 페이지를 다른 페이지로 연결하는 링크
- 참조를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트

## Markup Language
- 태그 등을 이용하여 문서나 데이터릐 구조를 명시하는 언어
    - HTML, Markdown

### Markup Language 예시
- 하이퍼 텍스트 마크업 언어는 웹 페이지 표시를 위해 개발된 지배적인 마크업 언어다. HTML은 제목, 단락, 목록 등과 같은 본문을 위한 구조적 의미를 나타내는 것뿐만 아니라 링크, 인용과 그 밖의 항목으로 구조적 문서를 만들 수 있는 방법을 제공한다. 그 안의 꺾쇠 괄호에 둘러싸인 "태그"로 되어있는 HTML 요소 형태로 작성한다. HTML은 웹 브라우저와 같은 HTML 처리 장치의 행동에 영향을 주는 자바스크립트, 본문과 그 밖의 항목의 외관과 배치를 정의하는 CSS 같은 스크립트를 포함하거나 불러올 수 있다. HTML과 CSS 표준의 공동 책임자인 W3C는 명확하고 표상적인 마크업을 위하여 CSS의 사용을 권장한다.

```html
<!-- 위의 문장을 html로 -->
<h1>HTML</h1>
<p>하이퍼 텍스트 마크업 언어는 웹 페이지 표시를 위해 개발된 지배적인 마크업 언어다.</p>
<p>본문 : HTML은 제목, 단락, 목록 등과 같은 본문을 위한 구조적 의미를 나타내는 것뿐만 아니라 링크, 인용과 그 밖의 항목으로 구조적 문서를 만들 수 있는 방법을 제공한다. 그 안의 꺾쇠 괄호에 둘러싸인 "태그"로 되어있는 HTML 요소 형태로 작성한다. HTML은 웹 브라우저와 같은 HTML 처리 장치의 행동에 영향을 주는 자바스크립트, 본문과 그 밖의 항목의 외관과 배치를 정의하는 CSS 같은 스크립트를 포함하거나 불러올 수 있다. HTML과 CSS 표준의 공동 책임자인 W3C는 명확하고 표상적인 마크업을 위하여 CSS의 사용을 권장한다.</p>
```

## HTML Element
```html
<p>This is HTML!</p>

<!-- <p> : Opening tag
    </p> : Closing tag
    This is HTML! : Content
    <p>This is HTML!</p> : Element
-->
```
- 하나의 요소는 여는 태그와 닫는 태그 그리고 그 안의 내용으로 구성됨
- 닫는 태그는 태그 이름 앞에 슬래시가 포함되며 닫는 태그가 없는 태그도 존재

## HTML Attribute
```html
<p class="editor-note">This is HTML!</p>

<!-- class="editor-note" : Attribute -->
```
- 규칙
    - 요소 이름 다음에 바로 오는 속성은 요소 이름과 속성 사이에 **공백**이 있어야 함
    - 하나 이상의 속성들이 있는 경우엔 속성 사이에 **공백**으로 구분함
    - 속성 값은 열고 닫는 **따옴표**로 감싸야 함

- 목적
    - 나타내고 싶지 않지만 추가적인 기능, 내용을 담고 싶을 때 사용
    - CSS가 해당 요소를 선택하기 위한 값으로 활용됨

## HTML 문서의 구조
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My page</title>
</head>
<body>
    <p>This is my page</p>
</body>
</html>
```
- !DOCTYPE html tag : 해당 문서가 html의 문서라는 것을 나타냄
- html tag : 전체 페이지의 콘텐츠를 포함
- title tag : 브라우저 탭 및 즐겨찾기 시 표시되는 제목으로 사용
- head tag
    - HTML 문서에 관련된 설명, 설정 등
    - 사용자에게 보이지 않음
- body tag : 페이지에 표시되는 모든 콘텐츠

## HTML Text structure
- HTML의 주요 목적 중 하나는 텍스트 구조와 의미를 제공하는 것
```html
<h1>Main Heading</h1>
```
- 예를 들어 h1 tag는 단순히 텍스트를 크게 만드는 것이 아닌 해당 **문서의 최상위 제목**이라는 의미를 부여하는 것

## 대표적인 HTML Text structure
- Heading & Paragraphs : h1 ~ 6, p
- Lists : ol, ul, li
    - Unordered
    - Ordered
- Emphasis & Importance : em, strong

---

## 참고
### HTML 관련 사항
- HTML 요소 이름은 대소문자를 구분하지 않지만 "소문자" 사용을 권장
- HTML 속성의 따옴표는 작은 따옴표와 큰 따옴표를 구분하지 않지만 "큰 따옴표" 권장
- HTML은 프로그래밍 언어와 달리 에러를 반환하지 않기 때문에 작성 시 주의