from django.contrib import admin
from .models import Article, BlogUser, Comment

# Register your models here.
admin.site.register(BlogUser)
admin.site.register(Article)
admin.site.register(Comment)
