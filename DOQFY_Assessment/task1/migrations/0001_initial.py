# Generated by Django 5.1 on 2024-08-23 17:24

import task1.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrlModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.URLField(max_length=500, unique=True, validators=[task1.models.custom_url_validator])),
                ('short_url', models.URLField()),
            ],
        ),
    ]
