# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='uaddress',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uphone',
            field=models.CharField(default='', max_length=11),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='ureceive',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uzip_code',
            field=models.CharField(default='', max_length=6),
        ),
    ]
