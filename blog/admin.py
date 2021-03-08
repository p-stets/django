from django.contrib import admin
from .models import Article, BlogUser, Comment, Like

# Register your models here.
admin.site.register(BlogUser)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Like)
