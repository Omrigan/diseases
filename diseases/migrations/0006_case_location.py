# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diseases', '0005_auto_20150516_0229'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='location',
            field=models.CharField(choices=[('1', 'Восточно-Сибирская'), ('2', 'Горьковская'), ('3', 'Дальневосточная'), ('4', 'Забайкальская'), ('5', 'Западно-Сибирская'), ('6', 'Калининградская'), ('7', 'Красноярская'), ('8', 'Куйбышевская'), ('9', 'Московская'), ('10', 'Октябрьская'), ('11', 'Приволжская'), ('12', 'Свердловская'), ('13', 'Северная'), ('14', 'Северо-Кавказская'), ('15', 'Юго-Восточная'), ('16', 'Южно-Уральская')], max_length=2, default='1'),
        ),
    ]
