# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homely', '0003_auto_20151007_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='giver',
            name='amount_given',
            field=models.DecimalField(default=0, max_digits=8, decimal_places=2),
        ),
    ]
