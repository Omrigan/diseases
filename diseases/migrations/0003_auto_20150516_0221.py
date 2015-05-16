# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diseases', '0002_case_disease'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='dateFinish',
            field=models.DateTimeField(verbose_name='Finish case', blank=True),
        ),
    ]
