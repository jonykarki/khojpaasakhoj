# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 06:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('khoj', '0003_auto_20171129_0729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='bphoneno',
            field=models.CharField(max_length=500),
        ),
    ]
