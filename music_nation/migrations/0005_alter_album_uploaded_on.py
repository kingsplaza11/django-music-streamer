# Generated by Django 4.0.4 on 2022-05-29 09:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_nation', '0004_auto_20181004_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='uploaded_on',
            field=models.DateField(default=datetime.datetime(2022, 5, 29, 9, 45, 50, 127783)),
        ),
    ]
