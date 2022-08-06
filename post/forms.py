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
          fields = ['name','body' ]
          widgets ={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),

          }