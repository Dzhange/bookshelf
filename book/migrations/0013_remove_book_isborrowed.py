# Generated by Django 2.0.7 on 2018-08-20 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0012_book_introduction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='IsBorrowed',
        ),
    ]
