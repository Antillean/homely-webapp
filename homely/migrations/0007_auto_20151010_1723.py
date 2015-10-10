# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('homely', '0006_auto_20151008_2358'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='charity',
            options={'ordering': ['created'], 'verbose_name_plural': 'charities'},
        ),
        migrations.AlterModelOptions(
            name='giver',
            options={'ordering': ['created']},
        ),
        migrations.AlterModelOptions(
            name='receiver',
            options={'ordering': ['created']},
        ),
        migrations.AddField(
            model_name='donation',
            name='donation_date',
            field=models.DateField(default=datetime.datetime(2015, 10, 10, 16, 22, 39, 301052, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='giver',
            name='email',
            field=models.EmailField(default='default@homely.test', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='giver',
            name='first_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='giver',
            name='last_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='giver',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='receiver',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
