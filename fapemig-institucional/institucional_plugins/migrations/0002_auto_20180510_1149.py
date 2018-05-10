# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-10 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institucional_plugins', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoamodel',
            name='cargo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pessoamodel',
            name='contato',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='pessoamodel',
            name='funcao',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pessoamodel',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='pessoamodel',
            name='info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pessoamodel',
            name='lates',
            field=models.URLField(blank=True, null=True),
        ),
    ]
