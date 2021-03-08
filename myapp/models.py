from django.db.models.deletion import PROTECT, SET_NULL
from myapp.views import first
from django.db import models
from django.db.models.fields import CharField

# Create your models here.


class Article(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField(null=True, blank=True)


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class Book(models.Model):
    name = models.CharField(max_length=120)
    author = models.ManyToManyField(Author, blank=True)
    reader = models.ForeignKey('BookUser', null=True, blank=True, on_delete=models.PROTECT)


class BookUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
