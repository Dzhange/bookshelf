# Generated by Django 2.0.6 on 2018-07-12 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_book_translator'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='FrontPage',
            field=models.URLField(default='static\no_frontpage.png', max_length=400),
        ),
    ]