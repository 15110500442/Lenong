# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('LenongGongsApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goodsinfo',
            name='gkucun',
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gpub_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 5, 15, 6, 8, 22, 881937)),
        ),
    ]
