# Generated by Django 3.1.6 on 2021-03-22 22:26

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=16)),
                ('pub_date', models.DateTimeField(verbose_name=datetime.datetime(2021, 3, 23, 0, 26, 36, 954756))),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=144)),
                ('votes', models.IntegerField(default=0)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='allstars.position')),
            ],
        ),
    ]
