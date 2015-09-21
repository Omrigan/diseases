# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diseases', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='disease',
            field=models.ForeignKey(default=0, to='diseases.Disease'),
            preserve_default=False,
        ),
    ]
