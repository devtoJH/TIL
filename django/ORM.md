# ORM(Object-Relational-Mapping)
    객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 데이터를 변환하는 프로그래밍 기술

## QuerySet API
- ORM에서 데이터를 검색, 필터링, 정렬 및 그룹화 하는데 사용하는 도구
- API를 사용하여 SQL이 아닌 Python 코드로 데이터를 처리

### QuerySet API 구문
- Article.objects.all()
    - Article : Model class
    - objects : Manager
    - all() : QuerySet API

### Query
- 데이터베이스에 특정한 데이터를 보여 달라는 요청
- "쿼리문을 작성한다."
    - 원하는 데이터를 얻기 위해 데이터베이스에 요청을 보낼 코드를 작성한다.
- 이 때, 파이썬으로 작성한 코드가 ORM에 의해 SQL로 변환되어 데이터베이스에 전달되며, 데이터베이스의 응답 데이터를 ORM이 QuerySet이라는 자료 형태로 변환하여 우리에게 전달

### QuerySet
- 데이터베이스에게서 전달 받은 객체 목록(데이터 모음)
    - 순회가 가능한 데이터로써 1개 이상의 데이터를 불러와 사용할 수 있음
- Django ORM을 통해 만들어진 자료형
- 단, 데이터베이스가 단일한 객체를 반환할 때는 QuerySet이 아닌 모델(Class)의 인스턴스로 반환됨

## QuerySet API 사전 준비
- 외부 라이브러리 설치 및 설정
```python
$ pip install ipython
$ pip install django-extensions
```
```python
# settings.py

INSTALLED_APPS = [
    'articles',
    'django_extensions',
    ...
]
```
```python
$ pip freeze > requirements.txt
```

## Django shell
- django 환경 안에서 실행되는 python shell
- 입력하는 QuerySet API 구문이 django 프로젝트에 영향을 미침

## 데이터 객체를 만드는(생성하는) 3가지 방법

### 첫 번째 방법(1/3)

```python
# 특정 테이블에 새로운 행을 추가하여 데이터 추가

>>> article = Article() # Article(class)로부터 article(instance)
>>> article
<Article: Article object (None)>

>>> article.title = 'first' # 인스턴스 변수(title)에 값을 할당
>>> article.content = 'django!' # 인스턴스 변수(content)에 값을 할당

# save를 하지 않으면 아직 DB에 값이 저장되지 않음
>>> article
<Article: Article object (None)>

>>> Article.objects.all()
<QuerySet []>
```

### 첫 번째 방법(2/3)
- **save 메서드를 호출해야 비로소 DB에 데이터가 저장 (레코드 생성)**
- save() : 객체를 데이터베이스에 저장하는 메서드

```python
# save를 하고 확인하면 저장된 것을 확인할 수 있다.

>>> article.save()
>>> article
<Article: Article object (1)>
>>> article.id
1
>>> article.pk
1
>>> Article.objects.all()
<QuerySet [Article: Article object (1)]>
```

### 첫 번째 방법(3/3)

```python
# 인스턴스인 article을 활용하여 변수에 접근(데이터 저장된 것을 확인)

>>> article.title
'first'
>>> article.content
'django!'
>>> article.created_at
datetime.datetime(2023, 1, 1, 2, 43, 56, 49345, tzinfo=<UTC>)
```

### 두 번째 방법

```python
>>> article = Article(title='second', content='django!')

# 아직 저장되어 있지 않음
>>> article
<Article: Article object (None)>

# save를 호출해야 저장됨
>>> article.save()
>>> article
<Article: Article object (2)>
>>> Article.objects.all()
<QuerySet [Article: Article object (1), Article: Article object (2)]>

# 값 확인
>>> article.pk
2
>>> article.title
'second'
>>> article.content
'django!'
```

### 세 번째 방법
- QuerySet API 중 create() 메서드 활용

```python
# 위 2가지 방식과는 다르게 바로 생성된 데이터가 반환된다.

>>> Article.objects.create(title='third', content='django1')
<Article: Article object (3)>
```

## ORM READ

### 1. 전체 데이터 조회

```python
# all() 메서드

>>> Article.objects.all()
<QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>]>
```

### 2. 단일 메서드 조회
- get()
    - 객체를 찾을 수 없으면 DoesNotExist 예외를 발생시키고, 둘 이상의 객체를 찾으면 MultipleObjectsReturned 예외를 발생시킴
    - **위와 같은 특징을 가지고 있기 때문에 primary key와 같이 고유성(uniqueness)을 보장하는 조회에서 사용해야 함**

```python
# get() 메서드

>>> Article.objects.get(pk=1)
<Article: Article object (1)>

>>> Article.objects.get(pk=100)
DoesNotExist: Article matching query does not exist.

>>> Article.objects.get(content='django!')
MultipleObjectsReturned: get() returned more than one Article -- it returned 2!
```

### 3. 특정 조건 데이터 조회

```python
# filter() 메서드

>>> Article.objects.filter(content='django!')
<QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>]>

>>> Article.objects.filter(title='a')
<QuerySet []>

>>> Article.objects.filter(title='first')
<QuerySet [<Article: Article object (1)>]>
```

## ORM UPDATE
- 데이터 수정

```python
# 수정할 인스턴스 조회
>>> article = Article.objects.get(pk=1)

# 인스턴스 변수를 변경
>>> article.title = '수정 제목'

# 저장
>>> article.save()

# 정상적으로 변경된 것을 확인
>>> article.title
'수정 제목'
```

## ORM DELETE
- 데이터 삭제

```python
# 삭제할 인스턴스 조회
>>> article = Article.objects.get(pk=1)

# delete 메서드 호출 (삭제된 객체가 반환)
>>> article.title = '수정 제목'

# 저장
>>> article.delete()
(1, {'articles.Article': 1})

# 삭제한 데이터는 더이상 조회할 수 없음
>>> Article.objects.get(pk=1)
DoesNotExist: Article matching query does not exist.
```