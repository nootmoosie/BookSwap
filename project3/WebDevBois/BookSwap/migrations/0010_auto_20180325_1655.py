# Generated by Django 2.0.2 on 2018-03-25 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookSwap', '0009_remove_book_isbn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(blank=True, choices=[('Fiction', 'Fiction'), ('Non-Fiction', 'Non-Fiction'), ('Textbook', 'Textbook'), ('History', 'History'), ('Mystery', 'Mystery'), ('Sci-Fi', 'Sci-Fi')], default='Fiction', help_text='Select a book genre (e.g. Science Fiction, French Poetry etc.)', max_length=200),
        ),
    ]
