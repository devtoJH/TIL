from django import forms
from .models import Review, Comment
# from .widgets import PreviewFileWidget

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'content', 'movie', 'image',)
    title = forms.CharField(
        label='제목',
        label_suffix='',
        widget=forms.TextInput(
            attrs={
                'placeholder': '제목',
                'max_length': 20,
                "class": "form-control",
                'style': 'width: 400px;'
            }
        ),
    )

    content = forms.CharField(
        label='내용',
        label_suffix='',
        widget=forms.Textarea(
            attrs={
                'placeholder': '내용',
                "class": "form-control",
                'style': 'width: 500px;'
            }
        ),
    )

    movie = forms.CharField(
        label='영화 제목',
        label_suffix='',
        widget=forms.TextInput(
            attrs={
                'placeholder': '영화 제목',
                'max_length': 20,
                "class": "form-control",
                'style': 'width: 400px;'
            }
        ),
    )
    # image = forms.ImageField(
    #     label='이미지',
    #     required=False,
    #     label_suffix='',
    #     widget=forms.FileInput(
    #         attrs={
    #             "class": "form-control",
    #             'style': 'width: 400px;'
    #         }
    #     ),
    # )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

    content = forms.CharField(
        label='댓글',
        label_suffix='',
        widget=forms.Textarea(
            attrs={
                'placeholder': '내용',
                "class": "form-control",
                'style': 'width: 600px; height: 100px;',   
            }
        ),
    )