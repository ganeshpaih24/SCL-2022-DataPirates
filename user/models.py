from unicodedata import name
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from post.models import Post
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about=models.CharField(max_length=25,null=True,blank=True)
    image = CloudinaryField('image')
    name = models.CharField(max_length=50, null=True, blank=True)
    profession = models.CharField(max_length=50,null=True, blank=True)
    followers = models.ManyToManyField("self", blank=True, related_name="following", symmetrical=False)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        #img = Image.open(self.image.path)

        # if img.height > 300 or img.width > 300:
        #     output_size = (300, 300)
        #     img.thumbnail(output_size)
        #     img.save(self.image.path)
