# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-02 01:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_userprofile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('staff_only', models.BooleanField(default=False)),
                ('slug', models.SlugField(null=True, unique=True)),
            ],
        ),
    ]
