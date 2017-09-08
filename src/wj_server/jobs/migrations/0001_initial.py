# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-06 14:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('seekers', '0002_auto_20170906_1412'),
        ('employers', '0003_auto_20170905_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_status', models.CharField(max_length=10)),
                ('applied_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=20)),
                ('job_type', models.CharField(max_length=20)),
                ('job_status', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=200)),
                ('opening_count', models.IntegerField(null=True)),
                ('urgent', models.BooleanField(default=False)),
                ('work_time', django_mysql.models.JSONField(default=dict, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('station', models.CharField(max_length=20, null=True)),
                ('incentive', models.CharField(max_length=100, null=True)),
                ('start_date', models.DateField(null=True)),
                ('hour_wage_low', models.IntegerField(null=True)),
                ('hour_wage_high', models.IntegerField(null=True)),
                ('req_gender', models.CharField(max_length=6, null=True)),
                ('req_education', models.CharField(max_length=20, null=True)),
                ('req_japanese_lang_level', models.IntegerField(null=True)),
                ('req_jlpt', models.IntegerField(null=True)),
                ('req_lang', django_mysql.models.ListCharField(models.CharField(max_length=10), max_length=110, size=10)),
                ('req_experience', django_mysql.models.ListCharField(models.CharField(max_length=10), max_length=55, size=5)),
                ('preferred_certification', django_mysql.models.ListCharField(models.CharField(max_length=10), max_length=110, size=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employers.Employer')),
            ],
        ),
        migrations.AddField(
            model_name='application',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.Job'),
        ),
        migrations.AddField(
            model_name='application',
            name='seeker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seekers.Seeker'),
        ),
    ]