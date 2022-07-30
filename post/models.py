from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.forms import ModelForm
#from tinymce import HTMLField

class Topic(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name


'''
class SubForm(ModelForm):
    class Meta:
        model = Form
        fields = ['name', 'authors']
'''

class Form(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE, unique=True)    
    description=models.TextField(null=True, blank=True)
    #subform=models.ForeignKey(SubForm,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.author


class Post(models.Model):
    topic=models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    title=models.CharField(max_length=100)
    form=models.ForeignKey(Form,on_delete=models.CASCADE)
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})

class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#    comment = HTMLField()