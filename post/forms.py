from django.forms import ModelForm
from django import forms
from post.models import Post,SubPost,Comment

class SubPostModelForm(ModelForm):
    class Meta:
        model = SubPost
        fields = ['title', 'description','resources']
        
class PostCommentForm(ModelForm):
      class Meta:
          model = Comment
          fields = ['body' ]

class PostForm(forms.ModelForm):  
    class Meta:
        model = Post
        fields = [
            "title",
            "image",
            "content",
        ]
          