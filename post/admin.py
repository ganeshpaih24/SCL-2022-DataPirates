from django.contrib import admin
from .models import Post,SubPost,Star,Category,Comment


admin.site.register(Post)
admin.site.register(SubPost)
admin.site.register(Category)
admin.site.register(Star)
admin.site.register(Comment)
