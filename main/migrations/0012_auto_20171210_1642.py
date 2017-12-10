# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-10 21:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20171205_2222'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notif', models.CharField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('sent_to', models.CharField(default='a', max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='bid_end_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 10, 16, 52, 23, 517557)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, default='\\static\\person-placeholder.jpg', upload_to='profile_image'),
        ),
    ]