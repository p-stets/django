from django.urls import include, path, re_path
from myapp.views import index, main_article, uniq_article, article, phone

from helpers import Cell

urlpatterns = [
    path('my_url/', include('myapp.urls')),
    path('', index, name='index'),
    path('article/', main_article, name='mail_article'),
    path('article/33/', uniq_article, name='uniq_article'),
    path('article/<int:article_id>/', article, name='article'),
    path('article/<int:article_id>/<slug:name>', article, name='article_name'),
    re_path(Cell.codes_regexp(), phone, name='phone'),
]
