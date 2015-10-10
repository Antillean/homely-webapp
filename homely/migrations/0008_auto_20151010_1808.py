# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import homely.models


class Migration(migrations.Migration):

    dependencies = [
        ('homely', '0007_auto_20151010_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='payment_token',
            field=models.CharField(default=homely.models.get_random_payment_token, unique=True, max_length=100),
        ),
    ]
