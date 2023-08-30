from django.db import models

class Genre(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Book(models.Model):
    title=models.CharField('Название', max_length=100)
    author=models.CharField('Автор', max_length=50)
    photo=models.ImageField(upload_to='static/img')
    date=models.DateTimeField('Дата публикации',auto_now=True)
    genre=models.ManyToManyField(Genre)

    def __str__(self):
        pass
        return 'Название книги - '+str(self.title)+' автор - '+str(self.author)+', описание - '+str(self.discription)

    class Meta:
        ordering=['title','author']

# >=    <атрибут>__gte
# <=    <атрибут>__lte
