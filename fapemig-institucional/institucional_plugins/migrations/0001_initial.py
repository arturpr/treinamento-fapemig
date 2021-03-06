# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-10 14:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0020_old_tree_cleanup'),
    ]

    operations = [
        migrations.CreateModel(
            name='PessoaModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='institucional_plugins_pessoamodel', serialize=False, to='cms.CMSPlugin')),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
