# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-04 12:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v_0_1', '0004_auto_20160310_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='arduinoid',
            field=models.CharField(default=b'QABN000001', max_length=99999999999L),
        ),
    ]