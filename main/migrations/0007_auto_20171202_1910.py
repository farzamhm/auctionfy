# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-03 00:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_room_productname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='productname',
        ),
        migrations.AddField(
            model_name='room',
            name='ID_product',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
