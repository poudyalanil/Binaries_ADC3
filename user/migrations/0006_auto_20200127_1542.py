# Generated by Django 3.0.2 on 2020-01-27 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20200127_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='country',
            field=models.CharField(default='Nepal', max_length=20),
        ),
        migrations.AlterField(
            model_name='customers',
            name='gender',
            field=models.CharField(max_length=20),
        ),
    ]
