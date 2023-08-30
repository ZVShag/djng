from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
from .models import Book
from .forms import book

def index(request):
    
    return render(request,'book/index.html')

def allbooks(request):
    bk=Book.objects.all()
    return render(request,'book/allbooks.html',{'list_book':bk,'title':'Информация о книгах'})

def book_inf(request,id):
    try:
        bk=Book.objects.filter(id=id)
        return render(request,'book/book_info.html', bk)
    except:
        return 

def Formbook(request):
    this_book=book()
    return render(request,'book/Add_book.html',{'form':this_book})

def Page_not_found(request,exception):
    return HttpResponseNotFound('<h1> Страница к котрой вы обратились не существует</h1>')