# Generated by Django 2.0.2 on 2018-04-19 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BookSwap', '0005_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='user_from',
            new_name='message_to',
        ),
    ]