from django import forms

class book(forms.Form):
    title = forms.CharField(max_length=100,help_text='Название книги')
    author = forms.CharField(max_length=50,help_text='Автор книги')
    photo = forms.ImageField()
    discription = forms.CharField(help_text='Описание')
    date = forms.DateTimeField(help_text='Дата публикации')