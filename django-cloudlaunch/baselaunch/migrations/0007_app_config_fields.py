# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-26 03:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baselaunch', '0006_public_services'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='default_launch_config',
            field=models.TextField(blank=True, help_text='Application-wide initial configuration data to parameterize the launch with.', max_length=16384, null=True),
        ),
        migrations.AddField(
            model_name='applicationversion',
            name='default_launch_config',
            field=models.TextField(blank=True, help_text='Version specific configuration data to parameterize the launch with.', max_length=16384, null=True),
        ),
        migrations.AlterField(
            model_name='applicationversioncloudconfig',
            name='default_launch_config',
            field=models.TextField(blank=True, help_text='Cloud specific initial configuration data to parameterize the launch with.', max_length=16384, null=True),
        ),
    ]
