# Generated by Django 2.0.2 on 2018-03-27 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BookSwap', '0015_remove_user_books_offered'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='books_offered',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='BookSwap.BookInstance'),
        ),
    ]
