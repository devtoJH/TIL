# Many to one relationships

## Foreign Key
- 테이블의 필드 중 다른 테이블의 레코드를 식별할 수 있는 키
- 각 레코드에서 서로 다른 테이블 간의 '관계'를 만드는 데 사용

## Comment & Article (모델 관계 설정)
## Many to one relationships (N:1 or 1:N)
- 한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 관계

### Comment(N) - Article(1)
- '0개 이상의 댓글을 1개의 게시글에 작성 될 수 있다.'

### ForeignKey()
- django에서 N:1 관계 설정 모델 필드

### Comment 모델 정의

```python
# articles/models.py

class Comment(models.Model):
    # 외래 키 필드
    article = models.ForeignKey(Article, on_delete=models.CASCADE) # CASCADE : 맨 위 게시글이 삭제되면 이 게시글에 작성된 댓글도 삭제됨(게시글이 존재해야 댓글도 존재함)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

- ForeignKey() 클래스의 인스턴스 이름은 참조하는 모델 클래스 이름의 단수형(소문자)으로 작성하는 것을 권장
- ForeignKey 클래스를 작성하는 위치와 관계없이 필드 마지막에 생성됨
- migrations 진행 후, comment 테이블 확인
    - article_id 필드 확인

#### ForeignKey(to, on_delete)
- to : 참조하는 모델 class 이름
- on_delete
    - 참조하는 모델 class가 삭제될 때, 연결된 하위 객체의 동작을 결정
    - 외래 키가 참조하는 객체(1)가 사라졌을 때, 외래 키를 가진 객체(N)를 어떻게 처리할 지를 정의하는 설정(데이터 무결성)
    - CASCADE
        - 부모 객체(참조된 객체)가 삭제 됐을 때 이를 참조하는 객체도 삭제
        - https://docs.djangoproject.com/en/3.2/ref/models/fields/#arguments

## Comment & Article (관계 모델 참조)

### 역참조
- 나를 참조하는 테이블(나를 외래 키로 지정한)을 참조하는 것
- N:1 관계에서는 1이 N을 참조하는 상황
- **하지만 Article에는 Comment를 참조할 어떠한 필드도 없다.**

### article.comment_set.all()
- article : 모델 인스턴스
- comment_set : related manager
- all() : QuerySet API

#### related manager
- N:1 혹은 M:N 관게에서 역참조 시에 사용하는 manager
- objects라는 매니저를 통해 queryset api를 사용했던 것처럼 related manager를 통해 queryset api를 사용할 수 있게 됨

#### related manager가 필요한 이유
- article.comment 형식으로는 댓글 객체를 참조할 수 없음
- 실제 Article 클래스에는 Comment와의 어떠한 관계도 작성되어 있지 않기 때문
- 대신 django가 역참조 할 수 있는 'comment_set' manager를 자동으로 생성해 article.comment_set 형태로 댓글 객체를 참조할 수 있음
- N:1 관계에서 생성되는 Related manager의 이름은 참조하는 **"모델명_set"** 이름 규칙으로 만들어짐

#### related manager 예시 (1/3)

```python
# shell_plus 실행 및 1번 게시글 조회

python manage.py shell_plus

article = Article.objects.get(pk=1)
```

#### related manager 예시 (2/3)

```python
# 1번 게시글에 작성된 모든 댓글 조회하기 (역참조)

>>> article.comment_set.all()
<QuerySet [<Comment: Comment object (1)>, <Comment: Comment object (2)>]>
```

#### related manager 예시 (3/3)

```python
# 1번 게시글에 작성된 모든 댓글 출력하기

comments = article.comment_set.all()

for comment in comments:
    print(comment.content)
```

## Comment & Article (댓글 기능 구현)
### Comment CREATE (1/6)

```python 
# articles/form.py

from .models import Article, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # 외래 키 필드는 사용자의 입력으로 받는 것이 아닌, view 함수 내에서 받아 별도로 처리해야 되어 저장되어야 하기 때문에 'content'로 설정함
        fields = ('content',)
```

### Comment CREATE (2/6)
- detail 페이지에서 CommentForm 출력 (view 함수)

```python 
# articles/views.py

from .forms import ArticleForm, CommentForm

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)
```

### Comment CREATE (3/6)
- detail 페이지에서 CommentForm 출력 (템플릿)

```html
<!-- articles/detail.html -->

<form action="#" method="POST">
    {% csrf_token %}
    {{ comment_form }}
    <input type="submit">
  </form>
```

### Comment CREATE (4/6)
- CommentForm 출력 확인

### Comment CREATE (5/6)
- 출력에서 제외된 외래 키 데이터는 어디서 받아와야 할까?
- detail 페이지의 url을 살펴보면 path('<int:pk>/', views.detail, name="detail") url에 해당 게시글의 pk 값이 사용되고 있음
- 댓글의 외래 키 데이터에 필요한 정보가 바로 게시글의 pk 값

### Comment CREATE (6/6)
```python
# articles/urls.py

urlpatterns = [
    ...
    path('<int:article_pk>/comments', views.comment_create, name='comment_create'),
]
```

```python
# articles/views.py

def comment_create(request, article_pk):
    # 몇 번 게시글인지 조회
    article = Article.objects.get(pk=article_pk)
    # 댓글 데이터를 받아서
    comment_form = CommentForm(request.POST)
    # 유효성 검사
    if comment_form.is_valid():
        # commit=False: 인스턴스는 반환하면서도 DB에 레코드는 작성하지 않도록 함
        comment = comment_form.save(commit=False) # save()에는 commit=True가 기본값으로 내장되어 있음
        comment.article = article
        comment_form.save()
        return redirect('articles:detail', article.pk)
    context = {
        'article': article,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)
```

```html
<!-- articles/detail.html -->

<form action="{% url 'articles:comment_create' article.pk %}" method="POST">
    {% csrf_token %}
    {{ comment_form }}
    <input type="submit">
  </form>
```

#### save(commit=False)
- "Create, but don't save the new instance."
- DB에 저장하지 않고 인스턴스만 반환
- https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/#the-save-method


### Comment READ (1/3)
- 전체 댓글 출력 (view 함수)

```python
# articles/views.py

from .models import Article, Comment

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    # 해당 게시글에 작성된 모든 댓글을 조회(역참조)
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)
```

### Comment READ (2/3)
- 전체 댓글 출력 (템플릿)

```html
<!-- articles/detail.html -->

<h4>댓글 목록</h4>
  <ul>
    {% for comment in comments %}
      <li>{{ comment.content }}</li>
    {% endfor %}
  </ul>
```

### Comment READ (3/3)
- 전체 댓글 출력 확인

### Comment DELETE (1/3)
- 댓글 삭제 url 작성

```python
# articles/urls.py

urlpatterns = [
    ...
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
]
```

### Comment DELETE (2/3)
- 댓글 삭제 view 함수 작성

```python
# articles/views.py

def comment_delete(request, article_pk, comment_pk):
    # 삭제할 댓글을 조회
    comment = Comment.objects.get(pk=comment_pk)
    # 댓글 삭제
    comment.delete()
    return redirect('articles:detail', article_pk)
```

### Comment DELETE (3/3)
- 댓글 삭제 버튼 작성

```html
<!-- articles/detail.html -->

<h4>댓글 목록</h4>
  <ul>
    {% for comment in comments %}
      <li>
        {{ comment.content }}
        <form action="{% url 'articles:comment_delete' article.pk comment.pk %}" method="POST">
          {% csrf_token %}
          <input type="submit" value="삭제">
        </form>
      </li>
    {% endfor %}
  </ul>
```

---

<br>

## 참고

### 댓글 개수 출력하기
- DTL filter - length 사용

```html
{{ comments|length }}

{{ article.comment_set.all|length }}
```

- Queryset API - count() 사용

```html
{{ article.comment_set.count }}
```

### 댓글이 없는 경우 대체 컨텐츠 출력
- DTL tag - for empty 사용

```html
<!-- articles/detail.html -->

<ul>
    {% for comment in comments %}
      <li>
        {{ comment.content }}
        <form action="{% url 'articles:comment_delete' article.pk comment.pk %}" method="POST">
          {% csrf_token %}
          <input type="submit" value="삭제">
        </form>
      </li>
    {% empty %}
        <p>댓글이 없습니다.</p>
    {% endfor %}
</ul>
```

### 댓글 수정을 구현하지 않는 이유
- 일반적으로 댓글 수정은 수정 페이지로 이동 없이 현재 페이지가 유지된 상태로 댓글 작성 Form 부분만 변경되어 수정할 수 있도록 함
- 이처럼 페이지의 일부 내용만 업데이트 하는 것은 JavaScript의 영역이기 때문

### admin site 등록
- 새로 작성한 Comment 모델을 admin site에 등록하기

```python
# articles/admin.py

from .models import Article, Comment

admin.site.register(Article)
admin.site.register(Comment)
```