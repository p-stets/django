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
    my_num = 33
    my_str = 'some string'
    my_dict = {"some_key": "some_value"}
    my_list = ['list_first_item', 'list_second_item', 'list_third_item']
    my_set = {'set_first_item', 'set_second_item', 'set_third_item'}
    my_tuple = ('tuple_first_item', 'tuple_second_item', 'tuple_third_item')
    my_class = MyClass('class string')
    return render(
        # Passing additional data to use in a django template
        request,
        template_name='index.html',
        context={
            'my_num': my_num,
            'my_str': my_str,
            'my_dict': my_dict,
            'my_list': my_list,
            'my_set': my_set,
            'my_tuple': my_tuple,
            'my_class': my_class,
            'display_num': True,
            'now': datetime.now(),
            'value': datetime.now()
        },
        content_type='text/html',
        status='200'
    )


def first(request):
    return render(request, 'first.html')


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
