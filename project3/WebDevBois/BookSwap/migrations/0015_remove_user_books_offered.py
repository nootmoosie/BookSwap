# Generated by Django 2.0.2 on 2018-03-27 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BookSwap', '0014_bookinstance_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='books_offered',
        ),
    ]
