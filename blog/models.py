from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.base import Model

# Create your models here.


class BlogUser(models.Model):
    '''
    A blog user
    '''

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Article(models.Model):
    '''
    A blog article
    '''

    title = models.CharField(max_length=250)
    content = models.TextField()
    author = models.ForeignKey(
        'BlogUser', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Article Author')

    def __str__(self):
        return self.title


class Comment(models.Model):
    '''
    A comment that is connected either to Article or to Comment
    '''

    author = models.ForeignKey('BlogUser', verbose_name=(
        "Comment author"), on_delete=models.SET_NULL, null=True, blank=True)
    article = models.ForeignKey('Article', verbose_name=(
        "Related Article"), on_delete=models.CASCADE)
    comment = models.ForeignKey(
        'self', verbose_name='Related Comment', on_delete=models.CASCADE)
    content = models.TextField(verbose_name='Content')

    def validate_related(self):
        if (self.article and self.comment) or (not self.article and not self.comment):
            raise ValidationError(
                'The comment should be connected either to article or to comment')

    def __str__(self):
        return f'{self.author}-{self.id}'


class Like(models.Model):
    owner = models.ForeignKey(BlogUser, verbose_name='Owner')


# Base comment approach

# class CommentLike(models.Model):
#     owner = models.ForeignKey(BlogUser, verbose_name='Owner')
#     comment = models.ForeignKey(
#         'Comment', on_delete=models.CASCADE, verbose_name='Related comment')


# class CommentDislike(models.Model):
#     owner = models.ForeignKey(BlogUser, verbose_name='Owner')
#     comment = models.ForeignKey(
#         'Comment', on_delete=models.CASCADE, verbose_name='Related comment')


# class ArticleLike(models.Model):
#     owner = models.ForeignKey(BlogUser, verbose_name='Owner')
#     article = models.ForeignKey(
#         'Article', on_delete=models.CASCADE, verbose_name='Related article')


# class ArticleDislike(models.Model):
#     owner = models.ForeignKey(BlogUser, verbose_name='Owner')
#     article = models.ForeignKey(
#         'Article', on_delete=models.CASCADE, verbose_name='Related article')
