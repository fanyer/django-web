# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-18 08:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogsPost',
        ),
    ]
