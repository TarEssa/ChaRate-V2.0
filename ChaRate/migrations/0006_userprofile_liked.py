# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-27 14:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ChaRate', '0005_auto_20180326_2329'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='liked',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ChaRate.Character'),
            preserve_default=False,
        ),
    ]