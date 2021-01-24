# Generated by Django 3.1.4 on 2021-01-24 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0003_auto_20210124_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videolikedislike',
            name='video',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='likedislikes',
                to='media.video',
            ),
        ),
    ]