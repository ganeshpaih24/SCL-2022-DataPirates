from django.db import models
<<<<<<< HEAD
from django.utils import timezone
=======
>>>>>>> c3769c453e2abe43eb38e12af9b47484cf2282b9
from django.contrib.auth.models import User

from PIL import Image

from post.models import Post


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
