# Generated by Django 3.0.2 on 2020-01-22 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='f_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customers',
            name='phone',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
