# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aptwi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='data_hora',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='resp_quest1',
            field=models.CharField(help_text=b'Digite a resposta', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='resp_quest2',
            field=models.CharField(help_text=b'Digite a resposta', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='resp_quest3',
            field=models.CharField(help_text=b'Digite a resposta', max_length=2, null=True),
        ),
    ]
