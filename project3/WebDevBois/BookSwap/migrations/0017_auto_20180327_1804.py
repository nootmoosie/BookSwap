# Generated by Django 2.0.2 on 2018-03-27 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BookSwap', '0016_user_books_offered'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='author',
            unique_together={('first_name', 'last_name')},
        ),
        migrations.AlterUniqueTogether(
            name='book',
            unique_together={('title', 'author')},
        ),
    ]