# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20160502154303 on 2016-05-19 15:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='centre',
            name='email',
            field=models.EmailField(default='jordi.martyn1@gmail.com', max_length=100),
        ),
        migrations.AlterField(
            model_name='centre',
            name='user',
            field=models.ManyToManyField(blank=True, default=None, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]