# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-15 03:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SerializerLearn', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_host', models.CharField(max_length=200)),
            ],
        ),
    ]
