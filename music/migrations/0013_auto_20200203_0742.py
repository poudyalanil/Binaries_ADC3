# Generated by Django 3.0.2 on 2020-02-03 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0012_auto_20200203_0740'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='albums',
            name='year',
        ),
        migrations.AddField(
            model_name='albums',
            name='artist',
            field=models.CharField(default='Unknown', max_length=250),
        ),
    ]
