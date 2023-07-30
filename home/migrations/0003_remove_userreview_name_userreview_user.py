# Generated by Django 4.2.3 on 2023-07-29 22:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_alter_suggesteddish_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userreview',
            name='name',
        ),
        migrations.AddField(
            model_name='userreview',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
