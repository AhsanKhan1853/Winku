# Generated by Django 5.0.2 on 2024-07-04 20:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 4, 20, 21, 0, 261654, tzinfo=datetime.timezone.utc)),
        ),
    ]
