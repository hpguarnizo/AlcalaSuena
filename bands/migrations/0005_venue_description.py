# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-18 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0004_auto_20170518_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
