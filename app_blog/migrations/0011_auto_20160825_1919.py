# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-25 17:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0010_auto_20160825_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateField(blank=True),
        ),
    ]
