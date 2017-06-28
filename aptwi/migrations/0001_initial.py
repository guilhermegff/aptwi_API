# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ra', models.CharField(help_text=b'Digite o seu RA', max_length=10)),
                ('nome_escola', models.CharField(help_text=b'Digite o nome da escola', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sugestao', models.CharField(help_text=b'Escreva sua sugestao', max_length=200, null=True)),
                ('data_hora', models.DateTimeField()),
                ('resp_quest1', models.CharField(help_text=b'Digite a resposta', max_length=1)),
                ('resp_quest2', models.CharField(help_text=b'Digite a resposta', max_length=1)),
                ('resp_quest3', models.CharField(help_text=b'Digite a resposta', max_length=1)),
                ('aluno', models.ForeignKey(to='aptwi.Aluno')),
            ],
        ),
        migrations.CreateModel(
            name='Questao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('questao', models.CharField(help_text=b'Escreva a questao', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('resposta', models.CharField(help_text=b'Escreva a resposta', max_length=200)),
                ('questao', models.ForeignKey(to='aptwi.Questao')),
            ],
        ),
    ]
