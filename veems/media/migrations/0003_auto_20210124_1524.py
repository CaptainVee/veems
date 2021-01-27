# Generated by Django 3.1.4 on 2021-01-24 15:24

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('media', '0002_videolikedislike'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='videolikedislike',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='videolikedislike',
            unique_together={('user', 'video')},
        ),
    ]