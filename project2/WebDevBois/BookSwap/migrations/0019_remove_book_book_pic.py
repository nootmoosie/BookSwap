# Generated by Django 2.0.2 on 2018-03-29 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BookSwap', '0018_auto_20180328_1610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book_pic',
        ),
    ]