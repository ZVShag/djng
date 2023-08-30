
from django.contrib import admin
from django.urls import path
from book.views import index,Page_not_found
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index,name='index'),
    #path('add',Formbook,name='form_book')
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

handler404=Page_not_found