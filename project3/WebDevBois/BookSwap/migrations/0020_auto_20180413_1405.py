# Generated by Django 2.0.2 on 2018-04-13 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BookSwap', '0019_remove_book_book_pic'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Profile',
        ),
        migrations.RemoveField(
            model_name='bookinstance',
            name='owner',
        ),
    ]
    atomic = False
