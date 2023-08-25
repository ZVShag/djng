from django.shortcuts import render
from django.http import HttpResponse
from library import urls

def index(request,title,author):
    return HttpResponse(f"""
    <p>Вы попали на страницу с описанием книги</p>
    <h1>{title}</h1>
    <h3> Автор: {author}</h3>""")
# схема(http,https,) body(byte string) method, encoding

def book(request):
    host=request.META['HTTP_HOST']
    uagent=request.META['HTTP_USER_AGENT']
    path=request.path

    return HttpResponse(f'Host: {host}\n UAgent: {uagent}\n Path: {path}')

def other(request):
    return render(request,'book/index.html')

    