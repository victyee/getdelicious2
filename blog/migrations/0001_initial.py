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
            name='BlogPicture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'blog/post_images/')),
                ('number', models.IntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(default=b'getdelicious', max_length=250)),
                ('title', models.CharField(max_length=350)),
                ('subtitle', models.CharField(max_length=350, null=True, blank=True)),
                ('post', django_markdown.models.MarkdownField(max_length=200000)),
                ('coverpicture', models.ImageField(null=True, upload_to=b'blog/coverpicture/', blank=True)),
                ('number', models.IntegerField(null=True, blank=True)),
                ('slug', models.SlugField(unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['timestamp'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='blogpicture',
            name='post',
            field=models.ForeignKey(to='blog.BlogPost'),
            preserve_default=True,
        ),
    ]
