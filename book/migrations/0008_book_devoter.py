# Generated by Django 2.0.7 on 2018-07-19 06:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0007_auto_20180719_0641'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='Devoter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
