from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    title = forms.CharField(
        label='Title',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': '제목을 입력해주세요.'
            }
        )
    )

    CHOICES = [('CS', 'CS'), ('개발', '개발'), ('신기술', '신기술')]

    category = forms.CharField(
        label='Category',
        widget=forms.Select(
            attrs={
                'class' : 'form-select',
                'type': 'select',
            },
            choices=CHOICES
        )
    )


    # option = forms.CharField(
    #     widget=forms.ModelFormOptions(
    #         attrs={
    #             'value':'1',
    #         }
    #     )
    # )    


    # ModelForm의 정보를 작성하는 곳
    class Meta:
        model = Post
        fields = '__all__'
        # fields = ('content',)
        # exclude = ('title',)        
