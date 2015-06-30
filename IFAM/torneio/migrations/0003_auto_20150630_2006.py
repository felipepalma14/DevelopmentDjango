# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('torneio', '0002_remove_curso_turno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='nome',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(b'^[a-zA-Z ]*$', b'Only letters are allowed')]),
        ),
        migrations.AlterField(
            model_name='curso',
            name='descricao',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(b'^[a-zA-Z ]*$', b'Only letters are allowed')]),
        ),
        migrations.AlterField(
            model_name='modalidade',
            name='descricao',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(b'^[a-zA-Z ]*$', b'Only letters are allowed')]),
        ),
        migrations.AlterField(
            model_name='turno',
            name='descricao',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(b'^[a-zA-Z ]*$', b'Only letters are allowed')]),
        ),
    ]
