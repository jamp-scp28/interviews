# Generated by Django 2.1.15 on 2020-07-15 17:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0012_auto_20200630_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 15, 17, 12, 10, 521743, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='apptest',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 15, 17, 12, 10, 521743, tzinfo=utc)),
        ),
    ]
