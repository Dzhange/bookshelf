# Generated by Django 2.0.7 on 2018-08-20 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0011_auto_20180719_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='Introduction',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
