# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Charity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'charities',
            },
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(max_digits=8, decimal_places=2)),
                ('payment_token', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Giver',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('photo', models.ImageField(null=True, upload_to=b'user/photo', blank=True)),
                ('facebook_id', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Receiver',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('photo', models.ImageField(null=True, upload_to=b'user/photo', blank=True)),
                ('beacon_id', models.CharField(max_length=100)),
                ('info', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='donation',
            name='giver',
            field=models.ForeignKey(to='homely.Giver'),
        ),
        migrations.AddField(
            model_name='donation',
            name='receiver',
            field=models.ForeignKey(to='homely.Receiver'),
        ),
        migrations.AddField(
            model_name='receiver',
            name='charity',
            field=models.ForeignKey(to='homely.Charity'),
        ),
    ]
