# Generated by Django 3.1.4 on 2021-01-02 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20210101_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='sync_videos_interested',
            field=models.BooleanField(default=False),
        ),
    ]