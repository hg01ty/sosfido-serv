# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-03 03:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0003_auto_20171001_1813'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='dni',
        ),
        migrations.RemoveField(
            model_name='person',
            name='gender',
        ),
    ]