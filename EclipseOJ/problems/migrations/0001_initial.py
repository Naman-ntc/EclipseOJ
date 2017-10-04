# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 09:16
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import problems.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contests', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_ID', models.CharField(max_length=10, unique=True)),
                ('number', models.CharField(max_length=1, validators=[django.core.validators.RegexValidator('^[A-Z]$', 'Only Captial letter is allowed.')])),
                ('name', models.CharField(max_length=40)),
                ('body', models.TextField()),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contests.Contest')),
            ],
            options={
                'verbose_name_plural': 'Problems',
            },
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testcase_body', models.FileField(upload_to=problems.models.testcases_directory_path)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problems.Problem')),
            ],
            options={
                'verbose_name_plural': 'TestCases',
            },
        ),
    ]