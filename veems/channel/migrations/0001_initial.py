# Generated by Django 3.1.4 on 2020-12-28 15:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import veems.common.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                (
                    'id',
                    veems.common.fields.ShortUUIDField(
                        default=veems.common.fields._default,
                        editable=False,
                        max_length=12,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    'created_on',
                    models.DateTimeField(auto_now_add=True, db_index=True),
                ),
                (
                    'modified_on',
                    models.DateTimeField(auto_now=True, db_index=True),
                ),
                ('name', models.CharField(max_length=60)),
                ('description', models.TextField(max_length=5000)),
                (
                    'visibility',
                    models.CharField(
                        choices=[
                            ('private', 'private'),
                            ('public', 'public'),
                            ('unlisted', 'unlisted'),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    'user',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                'ordering': ['created_on'],
                'abstract': False,
            },
        ),
    ]