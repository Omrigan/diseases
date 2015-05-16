# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diseases', '0004_auto_20150516_0223'),
    ]

    operations = [
        migrations.RenameField(
            model_name='disease',
            old_name='title',
            new_name='name',
        ),
    ]
