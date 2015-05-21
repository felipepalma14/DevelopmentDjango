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
                ('nomeAluno', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricaoCurso', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Modalidade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricaoModalidade', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TurnoCurso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricaoTurno', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='curso',
            name='cursoModalidade',
            field=models.ForeignKey(to='torneio.Modalidade'),
        ),
        migrations.AddField(
            model_name='curso',
            name='cursoTurno',
            field=models.ForeignKey(to='torneio.TurnoCurso'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='cursoAluno',
            field=models.ForeignKey(to='torneio.Curso'),
        ),
    ]
