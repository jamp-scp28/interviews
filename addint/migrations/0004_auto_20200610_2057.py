# Generated by Django 3.0.6 on 2020-06-11 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addint', '0003_auto_20200610_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addint',
            name='hire',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='addint',
            name='interviewed',
            field=models.BooleanField(),
        ),
    ]
