from django.urls import include, path, re_path
from myapp.views import index, main_article, uniq_article, article, phone
from django.contrib import admin

from myapp.helpers import codes_regexp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('my_url/', include('myapp.urls')),
    path('', index, name='index'),
    path('article/', main_article, name='main_article'),
    path('article/33/', uniq_article, name='uniq_article'),
    path('article/<int:article_id>/', article, name='article'),
    path('article/<int:article_id>/<slug:slug_text>/', article, name='article_name'),
    re_path(route=codes_regexp(), view=phone, name='phone'),  # Catch mobile no
]
