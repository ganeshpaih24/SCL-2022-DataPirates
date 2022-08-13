from django.forms import ModelForm
from django import forms
from post.models import Post, SubPost, Comment


class SubPostModelForm(ModelForm):
    class Meta:
        model = SubPost
        fields = ['title', 'description', 'resources']


class PostCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            "title",
            "image",
            "content",
        )
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ImageField(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
