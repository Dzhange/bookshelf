# Generated by Django 2.0.7 on 2018-08-23 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0017_auto_20180823_0414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowrecord',
            name='BeginTime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
