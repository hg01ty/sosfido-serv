# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-28 00:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0010_auto_20171027_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animalreport',
            name='pet_name',
            field=models.CharField(blank=True, default='Sin nombre', max_length=50, null=True),
        ),
    ]
