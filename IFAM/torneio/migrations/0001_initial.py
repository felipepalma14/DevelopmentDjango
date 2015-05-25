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
                ('nome', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Modalidade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='curso',
            name='modalidade',
            field=models.ForeignKey(to='torneio.Modalidade'),
        ),
        migrations.AddField(
            model_name='curso',
            name='turno',
            field=models.ForeignKey(to='torneio.Turno'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='curso',
            field=models.ForeignKey(to='torneio.Curso'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='turno',
            field=models.ForeignKey(to='torneio.Turno'),
        ),
    ]
