# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('dateStart', models.DateTimeField(verbose_name='Start case')),
                ('dateFinish', models.DateTimeField(verbose_name='Finish case')),
                ('description', models.CharField(max_length=4000)),
            ],
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('dateCreation', models.DateTimeField(verbose_name='date published')),
                ('description', models.CharField(max_length=4000)),
            ],
        ),
    ]
