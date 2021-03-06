# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SituacaoProjeto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('situacao', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='projeto',
            name='situacao',
            field=models.ForeignKey(to='gestaoapp.SituacaoProjeto'),
        ),
    ]
