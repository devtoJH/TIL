from django import forms
from .models import Post, Comment
from imagekit.forms import ProcessedImageField
from imagekit.processors import ResizeToFill, ResizeToCover, ResizeToFit

class PostForm(forms.ModelForm):
    image1 = ProcessedImageField(
        widget=forms.FileInput(
            attrs={
                "class": "form-control",
                'style': 'width: 400px;'
            }
        ),
        spec_id='posts:image1',
        processors=[ResizeToCover(200,200)],
        format='JPEG',
        options={'quality' : 80},
        required=False,
    )

    image2 = ProcessedImageField(
        widget=forms.FileInput(
            attrs={
                "class": "form-control",
                'style': 'width: 400px;'
            }
        ),
        spec_id='posts:image2',
        processors=[ResizeToFill(200,200)],
        format='JPEG',
        options={'quality' : 50},
        required=False,
    )

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': '제목을 입력해주세요.',
                'id': 'title',
            }
        )
    )

    select1_content = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': '',
                'id': 'content',
            }
        )
    )

    select2_content = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': '',
                'id': 'content',
            }
        )
    )
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['title'].widget.attrs['class'] = 'form-control'
    #     self.fields['title'].widget.attrs['style'] = 'background-color: rgb(23 32 54); border: 1px solid rgb(37 48 74); color: white;'

    class Meta:
        model = Post
        fields = ('title', 'select1_content', 'image1', 'select2_content', 'image2', )




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
                'style': 'width: 94%; height: 100px;',
            }
        ),
    )