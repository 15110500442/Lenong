# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('gtitle', models.CharField(max_length=20)),
                ('gpic', models.ImageField(upload_to='static/media/')),
                ('gprice', models.DecimalField(decimal_places=2, max_digits=5)),
                ('isDelete', models.BooleanField(default=False)),
                ('gclick', models.IntegerField(default=0)),
                ('gunit', models.CharField(default='500g', max_length=20)),
                ('gjianjie', models.CharField(max_length=200)),
                ('gkucun', models.IntegerField()),
                ('gcontent', models.TextField()),
                ('gpub_date', models.DateTimeField(verbose_name=datetime.datetime(2018, 5, 15, 3, 14, 45, 296062))),
                ('gpubj_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TypeInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('ttitle', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='gtype',
            field=models.ForeignKey(to='LenongGongsApp.TypeInfo'),
        ),
    ]
