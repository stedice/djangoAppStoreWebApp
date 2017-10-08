# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-07 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('platform', models.CharField(choices=[('i', 'iOS'), ('a', 'Android')], default='i', max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
