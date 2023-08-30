from django.db import models

class Book(models.Model):
    title=models.TextField(blank=False,max_length=200)
    author=models.TextField(blank=False,max_length=100)
    photo=models.ImageField(upload_to='')
     
