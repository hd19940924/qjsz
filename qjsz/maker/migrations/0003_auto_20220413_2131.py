# Generated by Django 3.2.13 on 2022-04-13 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maker', '0002_auto_20220413_0916'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.IntegerField(default=123456),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.IntegerField(default=123456),
        ),
    ]
