from django.forms import ModelForm
from django import forms
from post.models import SubPost,Comment

class SubPostModelForm(ModelForm):
    class Meta:
        model = SubPost
        fields = ['title', 'description','resources']
        
class PostCommentForm(ModelForm):
      class Meta:
          model = Comment
          fields = ['body' ]
          