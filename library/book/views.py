from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
from .models import Book
from .forms import book

def index(request):
    return render(request,'book/book_info.html', {'title': 'Информация о книге'})

def Formbook(request):
    this_book=book()
    return render(request,'Add_book.html',{'form':this_book})

def Page_not_found(request,exception):
    return HttpResponseNotFound('<h1> Страница к котрой вы обратились не существует</h1>')