from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth.decorators import login_required


def login(request):
    if request.user.is_authenticated:
        return redirect('posts:index')

    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('posts:index')
    else:
        form = LoginForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('posts:index')


def signup(request):
    if request.user.is_authenticated:
        return redirect('posts:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('posts:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@login_required
def profile(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)
    selects1 = person.selects1.all()
    selects2 = person.selects2.all()
    selects = (selects1 | selects2).distinct()
    print(selects)
    context = {
        'person': person,
        'selects': selects
    }
    return render(request, 'accounts/profile.html', context)