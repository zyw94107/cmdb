# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-28 17:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='name',
            field=models.CharField(max_length=128, unique=True, verbose_name='资产名称'),
        ),
    ]
