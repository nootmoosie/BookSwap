# Generated by Django 2.0.2 on 2018-03-25 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookSwap', '0007_auto_20180325_1640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookinstance',
            name='comments',
        ),
        migrations.AddField(
            model_name='bookinstance',
            name='comment',
            field=models.CharField(default='', help_text='Additional comments about your book (e.g. pricing, books you want to swap it for, etc).', max_length=500),
        ),
    ]
