from django.contrib import admin
from .models import Article, BlogUser, Comment, Like


class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_date', 'updated_date', )


class BlogUserAdmin(admin.ModelAdmin):
    readonly_fields = ('created_date', 'updated_date', )


class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ('created_date', 'updated_date', )


class LikeAdmin(admin.ModelAdmin):
    readonly_fields = ('created_date', 'updated_date', )


# Register your models here.
admin.site.register(BlogUser, BlogUserAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)
