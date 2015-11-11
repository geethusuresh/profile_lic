# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(null=True, blank=True)),
                ('address', models.TextField(null=True, blank=True)),
                ('phone', models.CharField(max_length=15, blank=True)),
                ('email', models.TextField(null=True, blank=True)),
                ('dob', models.DateField(null=True, blank=True)),
                ('age', models.IntegerField(default=0)),
                ('height', models.TextField(null=True, blank=True)),
                ('weight', models.TextField(null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Customer Data',
                'verbose_name_plural': 'Customer Data',
            },
        ),
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('policy_no', models.TextField(null=True, blank=True)),
                ('created_date', models.DateField(null=True, blank=True)),
                ('table', models.TextField(null=True, blank=True)),
                ('term', models.TextField(null=True, blank=True)),
                ('premium_amount', models.FloatField(default=0)),
                ('mode', models.TextField(null=True, blank=True)),
                ('nominee', models.TextField(null=True, blank=True)),
                ('nominee_address', models.TextField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Policy',
                'verbose_name_plural': 'Policy',
            },
        ),
    ]
