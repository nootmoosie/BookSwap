# Generated by Django 2.0.2 on 2018-03-25 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookSwap', '0003_auto_20180325_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='books_offered',
            field=models.ManyToManyField(help_text='THIS IS INCORRECT', related_name='_user_books_offered_+', to='BookSwap.Book'),
        ),
    ]
