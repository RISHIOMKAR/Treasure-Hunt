# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-10 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20161010_1639'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserScore',
            new_name='UserInfo',
        ),
        migrations.AddField(
            model_name='userlevelprogress',
            name='total_question_answered',
            field=models.IntegerField(default=0),
        ),
    ]
