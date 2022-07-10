from email.policy import default
from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User
from post.models import Post



class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

     