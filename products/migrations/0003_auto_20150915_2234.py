# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20150915_2222'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variation',
            old_name='extra_hours_charge_please_call_to_discuss',
            new_name='please_call_to_discuss',
        ),
        migrations.RemoveField(
            model_name='variation',
            name='extra_km_charge_please_call_to_discuss',
        ),
    ]
