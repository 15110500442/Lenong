# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('LenongGongsApp', '0002_auto_20180515_0608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsinfo',
            name='gpub_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 5, 16, 10, 48, 2, 872389)),
        ),
    ]
