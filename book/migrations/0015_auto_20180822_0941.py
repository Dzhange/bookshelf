# Generated by Django 2.0.7 on 2018-08-22 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0014_borrowrecord_finished'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowrecord',
            name='BeginTime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
