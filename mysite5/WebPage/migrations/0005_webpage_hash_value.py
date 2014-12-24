# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebPage', '0004_auto_20141223_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='webpage',
            name='hash_value',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
