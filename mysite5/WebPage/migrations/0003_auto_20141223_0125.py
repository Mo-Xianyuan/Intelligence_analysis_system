# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebPage', '0002_favour_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='webpage',
            name='dow_time',
            field=models.CharField(default=b'', max_length=20),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='webpage',
            name='pub_time',
            field=models.CharField(default=b'', max_length=20),
            preserve_default=True,
        ),
    ]
