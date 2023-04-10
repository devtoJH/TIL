## User 객체와 CUD
- 회원 가입
- 회원 탈퇴
- 회원정보 수정
- 비밀번호 변경

## 회원 가입
- User 객체를 Create 하는 것

### UserCreationForm()
- 회원 가입을 위한 built-in ModelForm

### 회원 가입 페이지 작성
```python
# accounts/url.py

app_name = 'accounts'
urlpatterns = [
    ...,
    path('signup/', views.signup, name='signup'),
]
```

```python
# accounts.views.py

def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/signup.html', context)
```

```html
<!-- accounts/signup.html -->

...
<h1>회원가입</h1>
<form action="{% url 'accounts:signup' %}" method='POST'>
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
</form>
...
```

### 회원가입 진행 후 에러 페이지 확인
- AttributeError...
- 회원가입에 사용하는 UserCreationForm이 우리가 대체한 커스텀 유저 모델이 아닌 기존 유저 모델로 인해 작성된 클래스이기 때문

```python
class Meta:
    model = User
    fields = ("username",)
    field_classes = {"username": UsernameField}
```

### 커스텀 유저 모델을 사용하려면 다시 작성해야 하는 forms
- UserCreationForm
- UserChangeForm
- => 두 form 모두 class Meta: model = User가 등록된 form이기 때문

```python
# django User 객체에 대한 직접 참조를 권장하지 않는다.
# from .models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # 현재 우리가 사용하는 User class로 재정의
        model = get_user_model()
```

#### get_user_model()
- 현재 프로젝트에서 활성화된 사용자 모델(active user model)을 반환하는 함수

### User 모델을 직접 참조하지 않는 이유
- User 모델을 get_user_model()을 사용해 참조하면 커스텀 User 모델을 자동으로 반환해주기 때문
- Django는 User 클래스를 직접 참조하는 대신 get_user_model()을 사용해 참조해야 한다고 강조

## 회원 탈퇴
- User 객체를 Delete 하는 것

### 회원 탈퇴 로직 작성
```python
# accounts/url.py

app_name = 'accounts'
urlpatterns = [
    ...,
    path('delete/', views.delete, name='delete'),
]
```

```python
# accounts.views.py

def delete(request):
    request.user.delete()
    return redirect('articles:index')
```

```html
<!-- accounts/index.html -->

...
<h1>회원탈퇴</h1>
<form action="{% url 'accounts:delete' %}" method='POST'>
    {% csrf_token %}
    <input type="submit" value='회원탈퇴'>
</form>
...
```

## 회원정보 수정
- User 객체를 Update 하는 것

### UserChangeForm()
- 회원 가입을 위한 built-in ModelForm

### 회원정보 수정 로직 작성
```python
# accounts/url.py

app_name = 'accounts'
urlpatterns = [
    ...,
    path('update/', views.update, name='update'),
]
```

```python
# accounts.views.py

def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        # form = CustomUserChangeForm(data = request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)
```

```html
<!-- accounts/index.html -->

...
<h1>회원정보 수정</h1>
<form action="{% url 'accounts:update' %}" method='POST'>
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
</form>
...
```

### UserChangeForm 사용 시 문제점
- 일반 사용자가 접근해서는 안 될 정보들(fields)까지 모두 수정이 가능해짐
- admin 인터페이스에서 사용되는 ModelForm이기 때문
- 따라서 CustomUserChangeForm에서 접근 가능한 필드를 조정해야 함

### CustomUserChangeForm fields 재정의

```python
# accounts/forms.py

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name',)
```

- User Model의 필드
- https://docs.djangoproject.com/en/3.2/ref/contrib/auth/

## 비밀번호 변경
- 비밀번호 변경 페이지
    - django는 비밀번호 변경 페이지를 회원정보 수정 form에서 별도 주소로 안내
        - /accounts/password/

### PasswordChangeForm()
- 비밀번호 변경을 위한 built-in Form

### 비밀번호 변경 페이지 작성
```python
# accounts/url.py

app_name = 'accounts'
urlpatterns = [
    ...,
    path('password/', views.change_password, name='change_password'),
]
```

```python
# accounts.views.py

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        # form = PasswordChangeForm(user = request.user, data = request.POST)
        if form.is_valid():
            user = form.save()
            # 비밀번호 변경 시, 세션 무효화 방지
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/change_password.html', context)
```

```html
<!-- accounts/change_password.html -->

...
<h1>비밀번호 변경</h1>
<form action="{% url 'accounts:change_password' %}" method='POST'>
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
</form>
...
```

### PasswordChangeForm의 인자 순서
- https://github.com/django/django/blob/stable/3.2.x/django/contrib/auth/forms.py

### 암호 변경 시 세션 무효화
- 비밀번호가 변경되는 기존 세션과의 회원 인증 정보가 일치하지 않게 되어 버려 로그인 상태가 유지되지 못함
- 비빌번호는 잘 변경되었으나 비빌번호가 변경되면서 기존 세션과의 회원 인증 정보가 일치하지 않기 때문

#### update_session_auth_hash(request, user)
- 암호 변경 시 세션 무효화 방지
- 암호가 변경되어도 로그아웃 되지 않도록 새로운 password의 session data로 기존 session을 업데이트

## 로그인 사용자에 대한 접근 제한
- 2가지 방법
    - is_authenticated : 속성
    - login_required : 데코레이터

### is_authenticated
- 사용자가 인증 되었는지 여부를 알 수 있는 User model의 속성
- 모든 User 인스턴스에 대해 항상 True인 읽기 전용 속성이며, AnonymousUser에 대해서는 항상 False임
- **권한(permission)과는 관련이 없으며, 사용자가 활성화 상태(active)이거나 유효한 세션(vaild session)을 가지고 있는지도 확인하지 않음**

### is_authenticated 적용하기 (1/2)
- 로그인과 비로그인 상태에서 출력되는 링크를 다르게 설정하기

```html
<!-- articles/index.html -->

{% if request.user.is_authenticated %}
<h3>안녕하세요, {{ user }} 님!</h3>
<form action="{% url 'accounts:logout' %}" method='POST'>
    {% csrf_token %}
    <input type="submit" value='Logout'>
</form>
<form action="{% url 'accounts:delete' %}" method='POST'>
    {% csrf_token %}
    <input type="submit" value='회원탈퇴'>
</form>
<a href="{% url 'accounts:update' %}">[회원정보수정]</a>
{% else %}
<a href="{% url 'accounts:login' %}">[login]</a>
<a href="{% url 'accounts:signup' %}">[회원가입]</a>
{% endif %}
```

### is_authenticated 적용하기 (2/2)
- 로그인과 비로그인 상태에서 출력되는 링크를 다르게 설정하기

```python
# accounts/views.py

def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    ...


def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    ...
```

### login_required
- 인증된 사용자에 대해서만 view 함수를 실행시키는 데코레이터
- 로그인 하지 않은 사용자의 경우 /accounts/login/ 주소로 redirect 시킴

### login_required 적용하기 (1/2)
- 인증된 사용자만 게시글을 작성/수정/삭제 할 수 있도록 수정

```python
# articles/views.py

from django.contrib.auth.decorators import login_required

@login_required
def create(request):
    pass


@login_required
def delete(request, article_pk):
    pass


@login_required
def update(request, article_pk):
    pass
```

### login_required 적용하기 (2/2)
- 인증된 사용자만 게시글을 로그아웃/탈퇴/수정/비밀번호 변경 할 수 있도록 수정

```python
# accounts/views.py

from django.contrib.auth.decorators import login_required

@login_required
def logout(request):
    pass


@login_required
def delete(request):
    pass


@login_required
def update(request):
    pass


@login_required
def change_password(request):
    pass
```

---

<br>

## 참고

### 데코레이터(Decorator)
- 기존에 작성된 함수에 기능을 추가하고 싶을 때, 해당 함수를 수정하지 않고 기능만을 추가해주는 함수

```python
def hello(func):
    def wrapper():
        print('HIHI')
        func()
        print('HIHI')
    return wrapper

@hello
def bye():
    print('byebye')

bye()

# 출력
HIHI
byebye
HIHI
```

### 회원가입 후 로그인까지 진행하려면
```python
# accounts/views.py

def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user) # 변수로 user로 둔 다음 auth_login 작성
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/signup.html', context)
```

### 탈퇴하면서 유저의 세션 정보도 함께 지우고 싶을 경우
```python
# accounts/views.py

def delete(request):
    request.user.delete()
    auth_logout(request) # 이 부분 추가
    return redirect('articles:index')
```

- "탈퇴(1) 후 로그아웃(2)"의 순서가 바뀌면 안됨
- 먼저 로그아웃 해버리면 해당 요청 객체 정보가 없어지기 때문에 탈퇴에 필요한 유저 정보 또한 없어지기 때문