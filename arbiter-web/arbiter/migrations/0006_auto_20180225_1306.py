# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-25 05:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arbiter', '0005_case_run_info_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='git_info',
            name='git_url',
            field=models.CharField(default='null', max_length=200),
        ),
        migrations.AlterField(
            model_name='case_run_info',
            name='deleted',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='case_run_info',
            name='result',
            field=models.CharField(default='FAILED', max_length=50),
        ),
    ]
