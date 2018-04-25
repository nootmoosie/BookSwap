# Generated by Django 2.0.2 on 2018-04-19 20:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BookSwap', '0004_remove_profile_books_offered'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, default='None', help_text='Message', max_length=200)),
                ('message_from', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='msg_from', to=settings.AUTH_USER_MODEL)),
                ('user_from', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='msg_to', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]