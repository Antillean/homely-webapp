# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homely', '0002_auto_20151003_1916'),
    ]

    operations = [
        migrations.AddField(
            model_name='receiver',
            name='amount_received',
            field=models.DecimalField(default=0, max_digits=8, decimal_places=2),
        ),
        migrations.AddField(
            model_name='receiver',
            name='amount_targeted',
            field=models.DecimalField(default=0, max_digits=8, decimal_places=2),
            preserve_default=False,
        ),
    ]
