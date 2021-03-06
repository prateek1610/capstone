# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-12 07:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='day',
            field=models.CharField(choices=[('MONDAY', 'MONDAY'), ('TUESDAY', 'TUESDAY'), ('WEDNESDAY', 'WEDNESDAY'), ('THURSDAY', 'THURSDAY'), ('FRIDAY', 'FRIDAY'), ('SATURDAY', 'SATURDAY'), ('SUNDAY', 'SUNDAY')], default=None, max_length=25),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='time',
            field=models.CharField(choices=[('BREAKFAST', 'BREAKFAST'), ('LUNCH', 'LUNCH'), ('DINNER', 'DINNER')], default=None, max_length=250),
        ),
    ]
