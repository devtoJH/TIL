# HTML form
    - 사용자로부터 form 요소를 통해 데이터를 받고 있으나 비정상적 혹은 악의적인 요청을 확인하지 않고 모두 수용중
    - 우리가 원하는 데이터 형식이 맞는지에 대한 '유효성 검증' 필요

## 유효성 검사
- 수집한 데이터가 정확하고 유효한지 확인하는 과정
- 유효성 검증에는 입력 값, 형식, 중복, 범위, 보안 등 부가적인 많은 것들을 고려해야 함
- 이런 과정과 기능을 제공해주는 **도구**가 필요

## Django Form
- 사용자 입력 데이터를 수집하고, 처리 및 유효성 검증을 수행하기 위한 도구
- **유효성 검사를 단순화하고 자동화 할 수 있는 기능을 제공**

### Form class 선언

```python
from django import forms

class TodoForm(forms.ModelForm):
    title = forms.CharField(max_length=10)
    content = forms.CharField()
```

### Form class를 적용한 new 로직

```python
from .forms import ArticleForm

def new(request):
    form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)
```

```html
<form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}

    <!--Form class -->
    {{ form }}

    <!-- Form rendering options -->
    {{ form.as_p }}

    <input type="submit">
  </form>
```

## Widgets
- HTML 'input' element의 표현을 담당
- 단순히 input 요소의 속성 및 출력되는 부분을 변경하는 것
- https://docs.djangoproject.com/ko/3.2/ref/forms/widgets/#built-in-widgets

## Django ModelForm
- Form
    - 사용자 입력 데이터를 DB에 저장하지 않을 때(ex. 로그인)
- ModelForm
    - 사용자 입력 데이터를 DB에 저장해야 할 때(ex. 회원가입)


### ModelForm class 선언

```python
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta: # ModelForm의 정보를 작성하는 곳
        model = Article
        fields = '__all__'
```

### fields 및 exclude 속성
- exclude 속성을 사용하여 모델에서 포함하지 않을 필드를 지정할 수도 있음

```python
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title',)
```
```python
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ('title',)
```

### ModelForm을 적용한 create 로직
- 코드 작성 후 적용 결과로 제목 input에 공백 값을 입력 후 에러 메세지 확인(유효성 검사)
```python
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

### is_valid()
- 여러 유효성 검사를 실행하고, 데이터가 유효한지 여부를 boolean으로 반환

### ModelForm을 적용한 edit 로직
```python
def edit(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/edit.html', context)
```
```html
<form action="{% url 'articles:update' article.pk %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="UPDATE">
</form>
```

### ModelForm을 적용한 update 로직
```python
def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    form = ArticleForm(request.POST, instance=article)
    if form.is_valid():
        form.save()
        return redirect('articles:detail', article.pk)
    context = {
        'form': form,
    }
    return render(request, 'articles/edit.html', context)
```

### save()
- 데이터베이스 객체를 만들고 저장
- 키워드 인자 instance 여부를 통해 생성할 지, 수정할 지를 결정

```python
# create
form = ArticleForm(request.POST)
form.save()

# update
form = ArticleForm(request.POST, instance=article)
form.save()
```

---

<br>

## 참고

### Widget 응용
```python
# forms.py
class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': '제목을 입력해주세요.',
            }
        ),
    )

    class Meta:
        model = Article
        fields = '__all__'
```

### Meta class?
- 클래스 안에 클래스? 파이썬에서는 Inner class 혹은 Nested class라고 하는데
- 파이썬의 문법적 개념으로 접근하지 말 것
- 단순히 모델 정보를 Meta라는 이름의 내부 클래스로 작성하도록 ModelForm의 설계가 이렇게 되어있을 뿐
- **ModelForm의 역할과 사용법을 숙지하는데 집중할 것**