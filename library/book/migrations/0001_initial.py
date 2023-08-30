# Generated by Django 4.2.4 on 2023-08-28 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=200)),
                ('author', models.TextField(max_length=100)),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
    ]