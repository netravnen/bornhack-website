# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-12 18:09


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0010_auto_20161212_1809'),
        ('camps', '0007_auto_20161212_1803'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Day',
        ),
    ]