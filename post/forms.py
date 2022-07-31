from django.forms import ModelForm

from post.models import SubPost

class SubPostModelForm(ModelForm):
    class Meta:
        model = SubPost
        fields = ['title', 'description','date_posted']