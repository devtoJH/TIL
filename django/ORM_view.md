# ORM with view

## 사전 준비
### app urls 분할 및 연결

```python
# articles/urls.py

from django.urls import path

app_name = 'articles'
urlpatterns = [
    
]
```
```python
# crud/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
]
```

### index 페이지 작성
```python
# articles/urls.py

from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
]
```
```python
# articles/views.py

def index(request):
    return render(request, 'articles/index.html')
```
```html
<!-- articles/index.html -->
<!-- body 태그 생략 -->

<h1>Articles</h1>
```

## READ(조회)

### 1. 전체 게시글 조회
```python
# articles/views.py

from .models import Article

def index(request):
    # DB에 전체 게시글 조회를 요청
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)
```
```html
<!-- articles/index.html -->

<h1>Articles</h1>
<hr>
{% for article in articles %}
    <p>글 번호: <a href="{% url 'articles:detail' article.pk %}">{{article.pk}}</a></p>
    <p>글 제목: {{article.title}}</p>
    <p>글 내용: {{article.content}}</p>
    <hr>
{% endfor %}
```

### 2. 단일 게시글 조회
```python
# articles/urls.py

app_name = 'articles'
urlpatterns = [
    ...
    path('<int:pk>/', views.detail, name='detail'),
]
```
```python
# articles/views.py

def detail(request, pk):
    article = Article.objects.get(pk=pk) # 왼쪽 pk: 컬럼, 오른쪽 pk: request 쪽 pk
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)
```
```html
<!-- articles/detail.html -->

<h1>Detail</h1>
<hr>
<p>글 번호: {{article.pk}}</p>
<p>제목: {{article.title}}</p>
<p>내용: {{article.content}}</p>
<p>작성일: {{article.created_at}}</p>
<p>수정일: {{article.updated_at}}</p>
<hr>
<a href="{% url 'articles:index' %}">[back]</a>
```

## CREATE
- create 로직을 구현하기 위해 필요한 view 함수
    1. new
    2. create

### 1. new
- 사용자의 입력을 받는 페이지를 렌더링

### new 로직 작성
```python
# articles/urls.py

app_name = 'articles'
urlpatterns = [
    ...
    path('new/', views.new, name='new'),
]
```
```python
# articles/views.py

def new(request):
    return render(request, 'articles/new.html')
```
```html
<!-- articles/new.html -->

<h1>New</h1>
<a href="{% url 'articles:index' %}">[메인 페이지]</a>
<form action="{% url 'articles:create' %}" method="GET">
    <div>
        <label for="title">제목:</label>
        <input type="text" name="title" id='title'>
    </div>
    <div>
        <label for="title">내용:</label>
        <textarea name="content" id="content" cols="30" rows="10"></textarea>
    </div>
    <input type="submit">
</form>
```

### 2. create
- 사용자가 입력한 데이터를 받아 DB에 저장

### create 로직 작성
```python
# articles/urls.py

app_name = 'articles'
urlpatterns = [
    ...
    path('create/', views.create, name='create'),
]
```
```python
# articles/views.py

def create(request):
    # new에서 보낸 사용자 데이터를 받아서 변수에 할당
    title = request.GET.get('title')
    content = request.GET.get('content')

    # 받은 데이터를 DB에 저장(3가지 방법)
    # 1.
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2. 2번이 가장 우수함
    article = Article(title=title, content=content)
    # 저장 전에 유효성 검사와 같은 추가 작업을 위해 2번 방법을 택함
    article.save()

    # 3.
    # Article.objects.create(title=title, content=content)

    # 결과 페이지 반환
    return render(request, 'articles/create.html')
```
```html
<!-- articles/create.html -->

<h1>게시글이 문제없이 작성되었습니다.</h1>
```