## HTTP requests 처리에 따른 view 함수 구조 변화

### new & create view 함수간 공통점과 차이점
- 공통점
    - 데이터 생성 로직을 구현하기 위함

- 차이점
    - new : GET method 요청만 처리
    - create : POST method 요청만 처리

## view 함수의 변화
- (GET) articles/create/ => 게시글 생성 페이지를 줘!
- (POST) articles/create/ => 게시글을 생성해줘!

### new와 create 함수 결합

```python
# 기존 new와 create함수

def new(request):
    form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)


def create(request):
    form = ArticleForm(request.POST)
    if form.is_valid():
        article = form.save()
        return redirect('articles:detail', article.pk)
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)
```
```python
# 기존 new와 create함수에서 결합된 코드

def create(request):
    # HTTP requests method가 POST라면
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    # POST가 아니라면
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)
```

### new url 정리
```python
app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    # path('new/', views.new, name='new'), => 불필요해진 new url 제거
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:artilce_pk>/delete/', views.delete, name='delete'),
    path('<int:article_pk>/edit/', views.edit, name='edit'),
    path('<int:article_pk>/update/', views.update, name='update'),
]
```

### 새로운 update view 함수
```python
# 기존 edit, update에서 결합된 코드

def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/edit.html', context)
```

### edit url 정리
```python
app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    # path('new/', views.new, name='new'), => 불필요해진 new url 제거
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:artilce_pk>/delete/', views.delete, name='delete'),
    # path('<int:article_pk>/edit/', views.edit, name='edit'), => 불필요해진 edit url 제거
    path('<int:article_pk>/update/', views.update, name='update'),
]
```