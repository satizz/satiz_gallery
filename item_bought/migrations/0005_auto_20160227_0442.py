# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-27 04:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item_bought', '0004_auto_20160227_0441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='date_sold',
            field=models.DateField(primary_key=True, serialize=False),
        ),
    ]