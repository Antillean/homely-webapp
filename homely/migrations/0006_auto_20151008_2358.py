# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homely', '0005_auto_20151008_2319'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='donation',
            options={'ordering': ['created']},
        ),
        migrations.RenameField(
            model_name='charity',
            old_name='created_at',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='charity',
            old_name='updated_at',
            new_name='updated',
        ),
        migrations.RenameField(
            model_name='donation',
            old_name='created_at',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='donation',
            old_name='updated_at',
            new_name='updated',
        ),
        migrations.RenameField(
            model_name='giver',
            old_name='created_at',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='giver',
            old_name='updated_at',
            new_name='updated',
        ),
        migrations.RenameField(
            model_name='receiver',
            old_name='created_at',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='receiver',
            old_name='updated_at',
            new_name='updated',
        ),
    ]
