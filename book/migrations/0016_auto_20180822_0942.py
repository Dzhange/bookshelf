# Generated by Django 2.0.7 on 2018-08-22 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0015_auto_20180822_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowrecord',
            name='BeginTime',
            field=models.DateTimeField(),
        ),
    ]
