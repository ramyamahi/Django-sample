# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-02 07:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_states'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Note',
        ),
    ]
