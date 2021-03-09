from datetime import datetime, timedelta
from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.base import Model

# Generic stuff import
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


# a = Comment.objects.all().order_by('-id').values('content')[:5]
# >>> Comment.objects.create(content='Finish', related_article_id=1, author_id=1)


class BlogUser(models.Model):
    '''
    A blog user
    '''

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Creation date')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='Last update date')

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
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Creation date')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='Last update date')

    def __str__(self):
        return f'{self.author} - {self.id}'


class Comment(models.Model):
    '''
    A comment that is connected either to Article or to Comment
    '''

    author = models.ForeignKey('BlogUser', verbose_name=(
        "Comment author"), on_delete=models.SET_NULL, null=True, blank=True)
    related_article = models.ForeignKey('Article', verbose_name=(
        "Related Article"), on_delete=models.CASCADE, null=True, blank=True)
    related_comment = models.ForeignKey(
        'self', verbose_name='Related Comment', on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField(verbose_name='Content')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Creation date')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='Last update date')
    # A validation to make sure either related_article or related_comment is populated; not both
    # and that the author is also present

    def save(self):
        year_before = datetime(
            year=datetime.now().year - 1,
            month=datetime.now().month,
            day=datetime.now().day,
            hour=datetime.now().hour,
            minute=datetime.now().minute,
            second=datetime.now().second
        )
        self.updated_date = year_before
        print(self.updated_date)
        yeear = self.objects.all().filter(id=self.id)
        print(yeear)

    def clean(self):
        if (self.related_article and self.related_comment) or (not self.related_article and not self.related_comment):
            connection_error_message = 'The comment should be connected either to article or to comment'
            raise ValidationError({
                'related_article': [connection_error_message, ],
                'related_comment': [connection_error_message, ]
            })
        if not self.author:
            raise ValidationError({
                'author': ['The author is required', ]
            })

    # Fancy name
    def __str__(self):
        return f'{self.author} - {self.id}'


# Generic way
class Like(models.Model):
    # Types of likes; either like of dislike
    LIKE = 1
    DISLIKE = 2

    TYPES = (
        (LIKE, 'Like'),
        (DISLIKE, 'Dislike')
    )

    type = models.PositiveSmallIntegerField(choices=TYPES, default=LIKE)
    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, related_name='activity_logs')
    object_id = models.BigIntegerField(default=None, null=True)
    object = GenericForeignKey(ct_field="content_type", fk_field="object_id")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Creation date')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='Last update date')


# Base comment way

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
