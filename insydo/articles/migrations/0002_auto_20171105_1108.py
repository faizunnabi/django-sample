# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-05 07:08
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=tinymce.models.HTMLField(),
        ),
    ]