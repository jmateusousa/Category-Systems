# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-10 13:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('importcsv', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subcategory',
            old_name='subcat',
            new_name='category_sub',
        ),
        migrations.RemoveField(
            model_name='category',
            name='subcat',
        ),
        migrations.AddField(
            model_name='channel',
            name='category_channel',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='importcsv.Category'),
            preserve_default=False,
        ),
    ]
