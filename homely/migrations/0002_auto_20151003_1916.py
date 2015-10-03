# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homely', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='payment_token',
            field=models.CharField(unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='giver',
            name='facebook_id',
            field=models.CharField(unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='receiver',
            name='beacon_id',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
