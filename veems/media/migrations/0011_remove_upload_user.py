# Generated by Django 3.1.4 on 2020-12-28 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0010_auto_20201228_2009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='user',
        ),
    ]