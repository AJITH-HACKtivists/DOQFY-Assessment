# Generated by Django 5.1 on 2024-08-24 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SnippetModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('secret_key', models.CharField(blank=True, max_length=256, null=True)),
                ('shareable_url', models.SlugField(unique=True)),
            ],
        ),
    ]
