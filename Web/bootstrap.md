# Bootstrap
    - 프론트엔드 라이브러리(Toolkit)
    - 반응형 웹 디자인 & CSS 및 JS 기반의 컴포넌트와 스타일 제공

## Bootstrap 기초
```html
<p class="mt-5">Hello, World!</p>
```
mt-5
- {property}{sides}-{size}

## Bootstrapl 속성
|  | property |
|:---:|:---:|
| m | margin | 
| p | padding |

---

|  | sides |
|:---:|:---:|
| t | top | 
| b | bottom |
| s | left | 
| e | right |
| y | top, bottom | 
| x | left, right |
| blank | 4 sides |

---

|  |  | size |
|:---:|:---:|:---:|
| 0 | 0 rem | 0px | 
| 1 | 0.25 rem | 4px |
| 2 | 0.5 rem |  8px |
| 3 | 1 rem | 16px |
| 4 | 1.5 rem |  24px |
| 5 | 3 rem | 48px |
| auto | auto | auto |

# Typography
    문서 상에 제목, 본문 텍스트, 목록 등
## Headings
```html
<!-- Headings -->
<p class="h1">h1. Bootstrap heading</p>
<p class="h2">h2. Bootstrap heading</p>
<p class="h3">h3. Bootstrap heading</p>
<p class="h4">h4. Bootstrap heading</p>
<p class="h5">h5. Bootstrap heading</p>
<p class="h6">h6. Bootstrap heading</p>
```
- HTML h1 ~ h6 태그와 스타일을 일치시키고 싶지만 관련 HTML태그를 더 사용할 수 없는 경우

## Display headings
```html
<!-- Display Headings -->
<p class="display-1">display 1</p>
<p class="display-2">display 2</p>
<p class="display-3">display 3</p>
<p class="display-4">display 4</p>
<p class="display-5">display 5</p>
<p class="display-6">display 6</p>
```
- 기존 Heading보다 더 눈에 띄는 제목이 필요할 경우(더 크고 약간 다른 스타일)

## Inline text elements
```html
<p>You can use the mark tag to <mark>highlight</mark> text.</p>
<p><del>This line of text is meant to be treated as deleted text.</del></p>
<p><s>This line of text is meant to be treated as no longer accurate.</s></p>
<p><ins>This line of text is meant to be treated as an addition to the document.</ins></p>
<p><u>This line of text will render as underlined.</u></p>
<p><small>This line of text is meant to be treated as fine print.</small></p>
<p><strong>This line rendered as bold text.</strong></p>
<p><em>This line rendered as italicized text.</em></p>
```
- HTML inline 요소에 대한 스타일

## List
```html
<ul class="list-unstyled">
    <li>This is a list.</li>
    <li>It appears completely unstyled.</li>
    <li>Structurally, it's still a list.</li>
    <li>However, this style only applies to immediate child elements.</li>
    <li>Nested lists:
      <ul>
        <li>are unaffected by this style</li>
        <li>will still show a bullet</li>
        <li>and have appropriate left margin</li>
      </ul>
    </li>
    <li>This may still come in handy in some situations.</li>
</ul>
```
- HTML list 요소에 대한 스타일

# Bootstrap Color system
    Bootstrap이 지정하고 제공하는 색상 시스템

## Colors
- Text, Border, Background 및 다양한 요소에 사용하는 Bootstrap의 색상 키워드

### Text colors
```html
<p class="text-primary">.text-primary</p>
<p class="text-primary-emphasis">.text-primary-emphasis</p>
<p class="text-secondary">.text-secondary</p>
<p class="text-secondary-emphasis">.text-secondary-emphasis</p>
<p class="text-success">.text-success</p>
<p class="text-success-emphasis">.text-success-emphasis</p>
<p class="text-danger">.text-danger</p>
```

### Background colors
```html
<div class="p-3 mb-2 bg-primary text-white">.bg-primary</div>
<div class="p-3 mb-2 bg-primary-subtle text-emphasis-primary">.bg-primary-subtle</div>
<div class="p-3 mb-2 bg-secondary text-white">.bg-secondary</div>
<div class="p-3 mb-2 bg-secondary-subtle text-emphasis-secondary">.bg-secondary-subtle</div>
<div class="p-3 mb-2 bg-success text-white">.bg-success</div>
<div class="p-3 mb-2 bg-success-subtle text-emphasis-success">.bg-success-subtle</div>
<div class="p-3 mb-2 bg-danger text-white">.bg-danger</div>
```

# Bootstrap Component
    - Bootstrap에서 제공하는 UI 관련 요소(버튼, 폼, 카드 등)
    - 일관된 디자인, 쉬운 프로토타입 제작 및 사용자 경험

## 대표 Component
- Alerts
- Badges
- Buttons
- Cards
- Navber

---

## 참고

## CDN(Content Delivery Network)
    - 지리적 제약 없이 빠르고 안전하게 콘텐츠를 전송할 수 있는 전송 기술
    - 서버와 사용자 사이의 물리적인 거리를 줄여 콘테츠 로딩에 소요되는 시간을 최소화(웹 페이지 로드 속도를 높임)

- 사용자가 해당 서버에서 멀리 떨어져 있는 경우 해당 콘텐츠를 로드하는 데 시간이 오래 걸림
- 지리적으로 사용자와 가까운 CDN 서버에 콘텐츠를 저장해서 사용자에게 절달