# Generated by Django 3.0.2 on 2020-01-16 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_auto_20200111_1726'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Album',
            new_name='Albums',
        ),
        migrations.RenameModel(
            old_name='Music',
            new_name='Musics',
        ),
    ]
