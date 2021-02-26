# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("It's index page!!")


def first(request):
    return HttpResponse("Hey! It's your first view!!")


def main_article(request):
    return HttpResponse('There will be a list with articles')


def uniq_article(request):
    return HttpResponse('This is uniq answer for uniq value')


def article(request, article_id, name=''):
    return HttpResponse(
        "This is an article #{}. {}".format(article_id, "Name of this article is {}".format(
            name) if name else "This is unnamed article"))


def phone(request, number):
    return HttpResponse(
        "<h1>Your phone {phone} is OK!!!!</h1>".format(phone=number)
    )


def zoom(request, *args):
    print(args)
    return HttpResponse(
        "<h1>Your combination is valid!!!</h1>"
    )
