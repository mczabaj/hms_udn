# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-09-28 00:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=3)),
                ('siblings', models.BooleanField(default=False)),
                ('env_exposures', models.CharField(blank=True, max_length=300)),
                ('genetic_mutations', models.CharField(blank=True, max_length=300)),
                ('status', models.CharField(choices=[('NR', 'Not Reviewed'), ('RA', 'Reviewed - Accepted'), ('RN', 'Reviewed - Not Accepted')], default='NR', max_length=2)),
            ],
        ),
    ]