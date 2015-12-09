# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OwnersSubmit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('food_truck_name', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=100)),
                ('owner_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=200)),
                ('message', models.TextField(max_length=1000, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
