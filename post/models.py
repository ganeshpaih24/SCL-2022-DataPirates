from datetime import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.forms import ModelForm
from PIL import Image
from ckeditor.fields import RichTextField
#from tinymce import HTMLField

class Category(models.Model):
    title = models.CharField(max_length=20)
    slug=models.SlugField()

    class Meta:
        verbose_name_plural='Categories'

    def __str__(self):
        return self.title


'''
class SubForm(ModelForm):
    class Meta:
        model = Form
        fields = ['name', 'authors']
'''

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    image = models.ImageField(default='wt-logo.png', upload_to='post_img')
    # content=models.TextField(null=True, blank=True)
    content = RichTextField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    stars_count= models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class SubPost(models.Model):
    post = models.ForeignKey(
        Post, related_name="subposts", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = RichTextField(blank=True, null=True)
    resources = models.TextField(max_length=1000, null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    '''
    class Meta:
        ordering=['-updated','-created']
    '''
    
    def __str__(self):
        return self.title
        
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
#    comment = HTMLField()
#    name=models.CharField(max_length=255)
    body=models.CharField(max_length=200)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    date_added=models.DateTimeField(auto_now_add=True)
    sno= models.AutoField(primary_key=True)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp= models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.body[0:50]

class Star(models.Model):
    posts=models.ManyToManyField(Post)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="star_user")
