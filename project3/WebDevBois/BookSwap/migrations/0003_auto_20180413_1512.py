# Generated by Django 2.0.2 on 2018-04-13 19:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BookSwap', '0002_remove_book_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
