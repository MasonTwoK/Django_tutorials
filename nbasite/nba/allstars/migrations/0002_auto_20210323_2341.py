# Generated by Django 3.1.6 on 2021-03-23 21:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allstars', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='position',
            old_name='position',
            new_name='pos_name',
        ),
        migrations.AlterField(
            model_name='position',
            name='pub_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 3, 23, 23, 41, 9, 265597)),
        ),
    ]