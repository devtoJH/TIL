from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = (
            'username',
            'email',
            'password1',
            'password2',
        )

    username = forms.CharField(label='아이디', label_suffix='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'style': 'width: 250px;'}))
    email = forms.EmailField(label='이메일', label_suffix='', widget=forms.EmailInput(
        attrs={'class': 'form-control', 'style': 'width: 250px;'}))
    password1 = forms.CharField(label='비밀번호', label_suffix='', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'style': 'width: 250px;'}))
    password2 = forms.CharField(label='비밀번호 확인', label_suffix='', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'style': 'width: 250px;'}))
    

class LoginForm(AuthenticationForm):
        username = forms.CharField(
            label="아이디",
            label_suffix='',
            required=True,
            widget=forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 250px;'})
        )

        password = forms.CharField(
            label="비밀번호",
            label_suffix='',
            widget=forms.PasswordInput(
                attrs={'class': 'form-control', 'style': 'width: 250px;'})
        ) 
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['email'].widget.attrs['class'] = 'form-control my-3'
    #     self.fields['username'].widget.attrs['class'] = 'form-control my-3'
    #     self.fields['password1'].widget.attrs['class'] = 'form-control my-3'
    #     self.fields['password2'].widget.attrs['class'] = 'form-control my-3'

    # username = forms.CharField(
    #     max_length=150, 
    #     required=True, 
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control', 
    #             'id': 'username',
    #             'aria-describedby': 'usernamehelp',
    #         }
    #     )
    # )
    # email = forms.EmailField(
    #     max_length=254, 
    #     required=True, 
    #     widget=forms.EmailInput(
    #         attrs={
    #             'class': 'form-control', 
    #             'id': 'email',
    #             'aria-describedby': 'emailhelp',
    #         }
    #     )
    # )
    # password1 = forms.CharField(
    #     label="Password", 
    #     widget=forms.PasswordInput(
    #         attrs={
    #             'class': 'form-control', 
    #             'id': 'password1',
    #             'aria-describedby': 'password1help',
    #         }
    #     )
    # )
    # password2 = forms.CharField(
    #     label="Password confirmation", 
    #     widget=forms.PasswordInput(
    #         attrs={
    #             'class': 'form-control', 
    #             'id': 'password2',
    #             'aria-describedby': 'password2help',
    #         }
    #     )
    # )

