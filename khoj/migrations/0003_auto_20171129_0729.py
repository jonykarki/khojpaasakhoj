# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-29 01:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('khoj', '0002_auto_20171128_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='bimg',
            field=models.URLField(),
        ),
    ]