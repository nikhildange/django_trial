# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-12 02:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employers', '0002_employer_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
