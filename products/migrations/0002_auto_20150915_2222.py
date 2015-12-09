# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='variation',
            name='extra_hours_charge_please_call_to_discuss',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='variation',
            name='extra_km_charge_please_call_to_discuss',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='variation',
            name='price_per',
            field=models.CharField(max_length=120, choices=[(b'guest', b'guest'), (b'hour', b'hour'), (b'serve', b'serve'), (b'minimum spend', b'minimum spend')]),
            preserve_default=True,
        ),
    ]
