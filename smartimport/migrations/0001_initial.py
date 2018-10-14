# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-10-11 13:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RawItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('item', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='item.TaggedItem')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
