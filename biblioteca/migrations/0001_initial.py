# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-12-01 20:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='livro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=200)),
                ('titulo', models.CharField(max_length=200)),
                ('isbn', models.CharField(max_length=200)),
                ('editora', models.CharField(max_length=200)),
            ],
        ),
    ]
