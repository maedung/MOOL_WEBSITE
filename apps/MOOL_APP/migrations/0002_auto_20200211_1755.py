# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-02-12 01:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MOOL_APP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='phone_number',
            field=models.CharField(max_length=255),
        ),
    ]
