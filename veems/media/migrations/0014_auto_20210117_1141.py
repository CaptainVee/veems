# Generated by Django 3.1.4 on 2021-01-17 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0013_auto_20210116_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='duration',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='framerate',
            field=models.IntegerField(null=True),
        ),
    ]
