# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('homely', '0004_giver_amount_given'),
    ]

    operations = [
        migrations.AddField(
            model_name='charity',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 8, 22, 19, 0, 730077, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='charity',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 8, 22, 19, 2, 849763, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='donation',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 8, 22, 19, 4, 929798, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='donation',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 8, 22, 19, 7, 40824, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='giver',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 8, 22, 19, 9, 184005, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='giver',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 8, 22, 19, 11, 32300, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='receiver',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 8, 22, 19, 12, 896053, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='receiver',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 8, 22, 19, 15, 23388, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
