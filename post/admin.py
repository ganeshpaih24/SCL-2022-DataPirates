from django.contrib import admin
from .models import Post,SubPost,Star


admin.site.register(Post)
admin.site.register(SubPost)
# admin.site.register(Topic)
admin.site.register(Star)
