from django.contrib import admin
from .models import Post,Comment,SubPost,Topic


admin.site.register(Post)
admin.site.register(SubPost)
admin.site.register(Topic)
admin.site.register(Comment)
