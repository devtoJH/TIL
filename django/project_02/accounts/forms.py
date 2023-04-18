from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import AbstractUser
from .models import User


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
    label='아이디',
    )
    email = forms.CharField(
    label='이메일',
    )
    first_name = forms.CharField(
    label='이름',
    )
    last_name = forms.CharField(
    label='성',
    )
    birthday = forms.CharField(
    label='생년월일',
    )
    password1 = forms.CharField(
    label='패스워드',
    )
    password2 = forms.CharField(
    label='패스워드 확인',
    )
    
    class Meta(UserCreationForm):

        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'birthday', 'password1', 'password2')
    



class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name')


# 실패 ㅠㅠ
# class AccountsForm(AbstractUser):
#     birthday = forms.CharField(
#         label='Birthday',
#         widget=forms.DateField(
#             attrs={
#                 'type':'date',
#                 'class':'form-control',
#             }
#         )
#     )

#     class Meta:
#         model = User
#         fields = '__all__'