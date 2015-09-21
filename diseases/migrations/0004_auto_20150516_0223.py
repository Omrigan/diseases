# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diseases', '0003_auto_20150516_0221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='dateFinish',
            field=models.DateTimeField(null=True, verbose_name='Finish case', blank=True),
        ),
    ]
