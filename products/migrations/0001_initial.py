# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('owner_name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=120)),
                ('contact_number', models.CharField(max_length=15, null=True, blank=True)),
                ('product_name', models.CharField(max_length=80)),
                ('logo', models.ImageField(null=True, upload_to=b'foodtruck/logo/', blank=True)),
                ('slogan', models.TextField(max_length=75, null=True, blank=True)),
                ('about_us', models.TextField(max_length=275, null=True, blank=True)),
                ('operating_state', models.CharField(max_length=120, choices=[(b'Victoria', b'Victoria'), (b'New South Wales', b'New South Wales'), (b'South Australia', b'South Australia'), (b'Queensland', b'Queensland'), (b'Western Australia', b'Western Australia'), (b'Australian Capital Territory', b'Australian Capital Territory'), (b'Northern Territory', b'Northern Territory'), (b'Tasmania', b'Tasmania')])),
                ('slug', models.SlugField(unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('active', models.BooleanField(default=False)),
                ('number', models.IntegerField(default=1, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('price_from', models.BooleanField(default=False)),
                ('price_per', models.CharField(max_length=120, choices=[(b'guest', b'guest'), (b'hour', b'hour'), (b'serve', b'serve')])),
                ('price', models.CharField(max_length=120)),
                ('minimum', models.CharField(max_length=120)),
                ('maximum', models.CharField(max_length=120)),
                ('included_travel_distance', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('maximum_travel_distance', models.DecimalField(default=0, null=True, max_digits=10, decimal_places=2, blank=True)),
                ('included_service_hours', models.DecimalField(default=0, null=True, max_digits=10, decimal_places=1, blank=True)),
                ('max_service_hours', models.DecimalField(default=0, null=True, max_digits=10, decimal_places=1, blank=True)),
                ('extra_km_not_available', models.BooleanField(default=False)),
                ('extra_hours_not_available', models.BooleanField(default=False)),
                ('extra_km_charge', models.DecimalField(default=0, null=True, max_digits=10, decimal_places=2, blank=True)),
                ('extra_hours_charge', models.DecimalField(default=0, null=True, max_digits=10, decimal_places=2, blank=True)),
                ('gluten_free_options_upon_request', models.BooleanField(default=False)),
                ('vegetarian_options_upon_request', models.BooleanField(default=False)),
                ('number', models.IntegerField(default=1, null=True, blank=True)),
                ('menu', django_markdown.models.MarkdownField(max_length=2000)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('product', models.ForeignKey(to='products.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
