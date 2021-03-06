# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-20 15:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monolith', '0030_printer_trashed_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='printer',
            options={'ordering': ('name', 'id')},
        ),
        migrations.AddField(
            model_name='printer',
            name='required_package',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='monolith.PkgInfoName'),
        ),
    ]
