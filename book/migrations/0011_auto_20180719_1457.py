# Generated by Django 2.0.7 on 2018-07-19 14:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0010_auto_20180719_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='Devoter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]