# Generated by Django 3.0.2 on 2020-01-10 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicLib', '0004_music_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='music',
            name='file',
        ),
    ]