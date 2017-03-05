# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0023_auto_20170218_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='video_recording',
            field=models.BooleanField(default=True, help_text='Whether the event will be video recorded.'),
        ),
        migrations.AddField(
            model_name='event',
            name='video_url',
            field=models.URLField(blank=True, help_text='URL to the recording.', max_length=1000, null=True),
        ),
    ]