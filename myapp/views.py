import random

from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render


class MyClass:
    string = ''

    def __init__(self, s):
        self.string = s


def index(request):
    '''
    Setting additional data
    '''

    def random_slug_text(min, max):
        '''
        Random text to use for random slug
        '''

        slug_chars = '0123456789abcdefghijklmnopqrstuvwxyz'  # Characters allowed for slug
        random_slug_text = ''.join(slug_chars[
            random.randint(0, len(slug_chars) - 1)]
            for i in range(0, random.randint(min, max))
        )
        return random_slug_text

    random_article_id = random.randint(1, 99999)

    return render(
        # Passing additional data to use in a django template
        request=request,
        template_name='index.html',
        context={
            'now': datetime.now(),
            'value': datetime.now(),
            'page_title': 'Homepage',
            'random_article_id': random_article_id,
            'random_slug_text': random_slug_text(5, 10)
        },
        content_type='text/html',
        status='200'
    )


def first(request):
    return render(request, 'first.html')


def main_article(request):
    return render(
        request,
        template_name='main_article.html',
        content_type='text/html',
        status='200',
        context={
            'page_title': 'Main Article'
        }
    )


def uniq_article(request):
    return render(
        request,
        template_name='unique_article.html',
        content_type='text/html',
        status='200'
    )


def article(request, article_id, slug_text=''):
    slug_text = slug_text
    article_id = article_id
    return render(
        request,
        template_name='article.html',
        content_type='text/html',
        status='200',
        context={
            'slug_text': slug_text,
            'article_id': article_id,
            'page_title': f'Article {article_id}'
        }
    )


def phone(request, number):
    return HttpResponse(
        "<h1>Your phone {phone} is OK!!!!</h1>".format(phone=number)
    )


def zoom(request, *args):
    print(args)
    return HttpResponse(
        "<h1>Your combination is valid!!!</h1>"
    )
