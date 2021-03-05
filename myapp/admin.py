from django.contrib import admin
from .models import Article, Author, Book, BookUser

admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookUser)
