# Generated by Django 3.0.2 on 2020-02-03 01:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0010_auto_20200122_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musics',
            name='music_genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='music.Genres'),
        ),
    ]