# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-11 18:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 11, 18, 35, 50, 142399, tzinfo=utc)),
        ),
    ]
