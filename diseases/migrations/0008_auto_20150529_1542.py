# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diseases', '0007_auto_20150518_0945'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='case',
            name='name',
            field=models.ForeignKey(to='diseases.Person'),
        ),
    ]
