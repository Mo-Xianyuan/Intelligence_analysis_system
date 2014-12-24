# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebPage', '0003_auto_20141223_0125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='website',
            name='domain',
        ),
        migrations.AddField(
            model_name='webpage',
            name='website',
            field=models.CharField(default=b'', max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='website',
            name='allowed_domain',
            field=models.CharField(default=b'', max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='website',
            name='start_url',
            field=models.CharField(default=b'', max_length=200),
            preserve_default=True,
        ),
    ]
