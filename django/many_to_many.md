# Many to many relationships (N:M or M:N)
    - 한 테이블의 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우
    - 양쪽 모두에서 N:1 관계를 가짐

## ManyToManyField(to, **options)
- many-to-many 관계 설정 시 사용하는 모델 필드
- 모델 필드의 RelatedManager를 사용하여 관련 개체를 추가, 제거 또는 생성
    - add(), remove(), create(), clear(), ...

### ManyToManyField's Arguments
#### 1. related_name
- 역참조시 사용하는 manager name을 변경

```python
class Patient(models.Model):
    doctors = models.ManyToManyField(Doctor, related_name='patients')
    name = models.TextField()
```
```python
# 변경 전
doctor.patient_set.all()

# 변경 후
doctor.patient.all()
```

#### 2. through
- 중개 테이블을 직접 작성하는 경우, through 옵션을 사용하여 중개 테이블을 나타내는 Django 모델을 지정
- 일반적으로 중개 테이블에 추가 데이터를 사용하는 다대다 관계와 연결하려는 경우(extra data with a many-to-many relationship)에 사용됨

#### 3. symmetrical
- ManyToManyField가 동일한 모델을 가리키는 정의에서만 사용
- 기본 값 : True
- True일 경우
    - _set 매니저를 추가하지 않음
    - source 모델의 인스턴스가 target 모델의 인스턴스를 참조하면 자동으로 target 모델 인스턴스도 source 모델 인스턴스를 자동으로 참조하도록 함(대칭)
    - 즉, 내가 상대방의 친구라면 상대방도 내 친구가 됨
        - ex) SNS 팔로워가 100만명이면 팔로우도 똑같이 100만명이 된다.

- 대칭을 원하지 않는 경우 False로 설정

```python
class Person(models.Model):
    friends = models.ManyToManyField('self')
    # friends = models.ManyToManyField('self', symmetrical=False)
```

### M:N에서의 methods
- add()
    - 지정된 객체를 관련 객체 집합에 추가
    - 이미 존재하는 관계에 사용하면 관계가 복제되지 않음

- remove()
    - 관련 객체 집합에서 지정된 모델 개체를 제거

## Article & User
### Article(M) - User(N)
- 0개 이상의 게시글은 0명 이상의 유저와 관련된다.
- **게시글은 유저로부터 0개 이상의 좋아요를 받을 수 있고, 유저는 0개 이상의 게시글에 좋아요를 누를 수 있다.**

### 모델 관계 설정 (1/5)
- ManyToManyField 작성

```python
# articles/models.py

class Article(models.Model):
    ...
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    ...
```

### 모델 관계 설정 (2/5)
- Migration 진행 후 에러 확인

![](./images/mtm_error.png)

### 모델 관계 설정 (3/5)
- like_users 필드 생성 시 자동으로 역참조에는 .article_set 매니저가 생성됨
- 그러나 이전 N:1(Article-User) 관계에서 이미 해당 매니저를 사용 중
    - user.article_set.all() -> 해당 유저가 작성한 모든 게시글 조회
    - user.article_set
        - N:1 => 유저가 작성한 게시글
        - M:N => 유저가 좋아요 한 게시글
- user가 작성한 글들 (user.article_set)과 user가 좋아요를 누른 글(user.article_set)을 구분할 수 없게 됨
    - **related_namager 이름이 충돌**
- user와 관계된 ForeignKey 혹은 ManyToManyField 중 하나에 related_name을 작성해야 함

### 모델 관계 설정 (4/5)
- related_name 작성 후 Migration

```python
# articles/models.py

class Article(models.Model):
    ...
    # related_name='like_articles'로 충돌나지 않게 이름 지정
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    ...
```

### 모델 관계 설정 (5/5)
- 생성된 중개 테이블 확인(aritcles_article_like_users)

### User - Article간 사용 가능한 related manager 정리
- article.user
    - 게시글을 작성한 유저 - N:1

- user.article_set
    - 유저가 작성한 게시글(역참조) - N:1

- article.like_users
    - 게시글을 좋아요한 유저 - M:N

- user.like_articles
    - 유저가 좋아요한 게시글(역참조) - M:N

### 좋아요 구현 (1/4)
- url 및 view 함수 작성

```python
# articles/urls.py

urlpatterns = [
    ...,
    path('<int:article_pk>/likes/', views.likes, name='likes'),
]
```
```python
# articles/views.py

@login_required
def likes(request, article_pk):
    # 좋아요를 누르는 대상 게시글
    article = Article.objects.get(pk=article_pk)

    # 좋아요 관계를 추가 or 삭제
    # case 1. 현재 좋아요를 요청하는 유저가 해당 게시글의 좋아요를 누른 유저 목록에 있는지 없는지를 확인
    if request.user in article.like_users.all():
    # case 2. 해당 게시글의 좋아요를 누른 유저에서 현재 요청하는 유저의 존재를 조회
    # if article.like_users.filter(pk=request.user.pk).exists():
        # 좋아요 취소
        article.like_users.remove(request.user)
    else:
        # 좋아요 추가
        article.like_users.add(request.user)
    return redirect('articles:index')
```

### 좋아요 구현 (2/4)
- index 템플릿에서 각 게시글을 좋아요 버튼 출력

```html
<!-- articles/index.html -->

{% for article in articles %}
    ...
    <form action="{% url 'articles:likes' article.pk %}" method="POST">
      {% csrf_token %}
      <!-- 현재 좋아요를 요청하는 유저가 게시글의 좋아요를 눌렀다면 -->
      {% if request.user in article.like_users.all %}
      <input type="submit" value="좋아요 취소">
      <!-- 현재 좋아요를 요청하는 유저가 게시글의 좋아요를 누르지 않았다면 -->
      {% else %}
      <input type="submit" value="좋아요">
      {% endif %}
    </form>
{% endfor %}
```

### 좋아요 구현 (3/4)
- 좋아요 버튼 출력 확인

### 좋아요 구현 (4/4)
- 좋아요 버튼 클릭 후 테이블 확인

### Profile 구현 (1/4)
- 자연스러운 follow 흐름을 위한 프로필 페이지 작성

```python
# accounts/urls.py

urlpatterns = [
    ...,
    # path('<username>/', views.profile, name='profile'),
    # 앞에 문자열로 url를 작성하면 위의 url 아래로 어떠한 url이 와도 <username>으로 간다.
    path('profile/<username>/', views.profile, name='profile'),
]
```
```python
# accounts/views.py

from django.contrib.auth import get_user_model

def profile(request, username):
    User = get_user_model()
    # 변수명을 person이라고 지은 이유
    # 이미 user라는 변수를 사용하고 있기 때문에(내장 변수) 구분하기 쉽지 않음
    person = User.objects.get(username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)
```

### Profile 구현 (2/4)
- profile 템플릿 작성

```html
<!-- accounts/profile.html -->

<h1>Profile</h1>
<button><a href="{% url 'articles:index' %}">back</a></button>
<h2>{{ person.username }}의 프로필 페이지</h2>
<hr>
<h2>{{ person.username }}가 작성한 모든 게시글</h2>
{% for article in person.article_set.all %}
    <div>{{ article.title }}</div>
{% endfor %}
<hr>
<h2>{{ person.username }}가 작성한 모든 댓글</h2>
{% for comment in person.comment_set.all %}
    <div>{{ comment.content }}</div>
{% endfor %}
<hr>
<h2>{{ person.username }}가 좋아요를 누른 모든 게시글</h2>
{% for article in person.like_articles.all %}
    <div>{{ article.title }}</div>
{% endfor %}
```

### Profile 구현 (3/4)
- Profile 템플릿으로 이동할 수 있는 하이퍼링크 작성

```html
<!-- articles/index.html -->

<a href="{% url 'accounts:profile' user.username%}">내 프로필</a>

{% for article in articles %}
    <p>작성자: 
      <a href="{% url 'accounts:profile' article.user.username %}">{{ article.user }}</a>
    </p>
{% endfor %}
```

### Profile 구현 (4/4)
- 출력 확인

## User & User (Follow 구현)
### User(M) - User(N)
- 유저는 0명 이상의 다른 유저와 관련된다.
- **유저는 다른 유저로부터 0개 이상의 팔로우를 받을 수 있고, 유저는 0명 이상의 다른 유저들에게 팔로잉 할 수 있다.**

### Follow 구현 (1/5)
- ManyToManyField 작성 및 Migration 진행

```python
# accounts/models.py

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
```

### Follow 구현 (2/5)
- 중개테이블 필드 확인
    - id, from_user_id, to_user_id 필드 확인

### Follow 구현 (3/5)
- url 및 view 함수 작성

```python
# accounts/urls.py

urlpatterns = [
    ...,
    path('<int:user_pk>/follow/', views.follow, name='follow'),
]
```
```python
# accounts/views.py

@login_required
def follow(request, user_pk):
    # 팔로우를 할 대상이 필요
    User = get_user_model()
    person = User.objects.get(pk=user_pk)

    # 팔로우 or 언팔로우
    # 내 계정은 팔로우 할 수 없음
    if person != request.user:
        # if person.followers.filter(pk=request.user.pk).exists():
        if request.user in person.followers.all():
            # 언팔로우
            person.followers.remove(request.user)
        else:
            # 팔로우
            person.followers.add(request.user)
    return redirect('accounts:profile', person.username)
```

### Follow 구현 (4/5)
- 프로필 유저의 팔로잉, 팔로워 수 & 팔로우, 언팔로우 버튼 작성

```html
<!-- accounts/profile.html -->

<div>
    팔로잉 : {{ person.followings.all|length }} / 팔로워 : {{ person.followers.all|length }}
</div>
{% if request.user != person %}
<div>
    <form action="{% url 'accounts:follow' person.pk %}" method="POST">
        {% csrf_token %}
        {% if request.user in person.followers.all %}
            <input type="submit" value='언팔로우'>
        {% else %}
            <input type="submit" value='팔로우'>
        {% endif %}
    </form>
</div>
{% endif %}
```

### Follow 구현 (5/5)
- 팔로우 버튼 클릭 후 팔로우 버튼 변화 및 중개 테이블 데이터 확인

---

<br>

## 참고
### .exists()
- QuerySet에 결과가 포함되어 있다면 True를 반환하고 그렇지 않다면 False를 반환
- 특히 큰 QuerySet에 있는 특정 개체의 존재와 관련된 검색에 유용

#### exists() 적용
```python
# articles/views.py

# 변경 전

@login_required
def likes(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.user in article.like_users.all():
        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)
    return redirect('articles:index')
```
```python
# articles/views.py

# 변경 후

@login_required
def likes(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if article.like_users.filter(pk=request.user.pk).exists():
        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)
    return redirect('articles:index')
```