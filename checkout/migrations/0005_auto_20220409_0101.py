# Generated by Django 3.2.12 on 2022-04-09 01:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_auto_20220409_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 9, 1, 1, 32, 5362, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='updatd_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 9, 1, 1, 32, 5399, tzinfo=utc)),
        ),
    ]
