# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-30 10:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viewflow', '0006_i18n'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyPizzaProcess',
            fields=[
                ('process_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='viewflow.Process')),
                ('content', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('viewflow.process',),
        ),
    ]
