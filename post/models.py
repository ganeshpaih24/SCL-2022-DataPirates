from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.forms import ModelForm
#from tinymce import HTMLField

# class Topic(models.Model):
#     name = models.CharField(max_length=200)
#     def __str__(self):
#         return self.name


'''
class SubForm(ModelForm):
    class Meta:
        model = Form
        fields = ['name', 'authors']
'''

class Post(models.Model):
    # topic=models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    title=models.CharField(max_length=100)
    content=models.TextField(null=True, blank=True)
    #subpost=models.ForeignKey(Post,on_delete=models.CASCADE)  
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})

class SubPost(models.Model):
    post=models.ForeignKey(Post,related_name="subposts", on_delete=models.CASCADE)  
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=1000,null=True, blank=True)
    resources=models.TextField(max_length=1000,null=True, blank=True)
    date_posted=models.DateTimeField(default=timezone.now)
    
    '''
    class Meta:
        ordering=['-updated','-created']
    '''
    
    def __str__(self):
        return self.title
        
class Comment(models.Model):
    post = models.ForeignKey(Post,related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
#    comment = HTMLField()
#    name=models.CharField(max_length=255)
    body=models.CharField(max_length=200)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]