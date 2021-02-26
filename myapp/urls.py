from django.urls import path, re_path

from .views import first, zoom

urlpatterns = [
    path('', first, name='first'),
    re_path(r'^zoom/[0-9A-Fa-f]{4}-.{6}/$', zoom, name='zoom'),  # catch /34f1-1ac498/
]
