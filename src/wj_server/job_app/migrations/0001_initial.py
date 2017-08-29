# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 06:51
from __future__ import unicode_literals

from django.db import migrations, models
import django_mysql.models


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
                ('skill', django_mysql.models.ListCharField(models.CharField(max_length=10), max_length=110, size=10)),
                ('address_coordinate', django_mysql.models.JSONField(default=dict)),
            ],
        ),
    ]
