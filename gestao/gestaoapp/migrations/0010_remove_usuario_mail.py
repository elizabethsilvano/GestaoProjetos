# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0009_auto_20150914_1740'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='mail',
        ),
    ]
