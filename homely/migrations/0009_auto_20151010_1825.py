# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('homely', '0008_auto_20151010_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receiver',
            name='amount_targeted',
            field=models.DecimalField(max_digits=8, decimal_places=2, validators=[django.core.validators.MinValueValidator(10)]),
        ),
    ]
