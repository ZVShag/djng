
from django.contrib import admin
from django.urls import path,re_path
from book.views import book,index,other
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('', index,kwargs={'title':'metro2035','author':'Gluhovskii'}),
    re_path('other', other),
    re_path('book', book)
] +static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
# 127.0.0.1:8000/book/hfdskfdkjsfh/thtrtrht/123231/tgrgr