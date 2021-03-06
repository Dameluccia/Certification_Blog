# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-23 21:06
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0002_auto_20160823_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from=models.CharField(max_length=120, unique=True), unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=120, unique=True),
        ),
    ]
