# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=20)),
                ('job_type', models.CharField(max_length=20)),
            ],
        ),
    ]
