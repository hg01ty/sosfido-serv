# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-21 01:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0008_auto_20171021_0039'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animalreport',
            old_name='location',
            new_name='place',
        ),
    ]
