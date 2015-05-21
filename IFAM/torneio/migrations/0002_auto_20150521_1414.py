# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('torneio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso',
            old_name='descricaoCurso',
            new_name='descricao',
        ),
        migrations.RenameField(
            model_name='modalidade',
            old_name='descricaoModalidade',
            new_name='descricao',
        ),
        migrations.RenameField(
            model_name='turnocurso',
            old_name='descricaoTurno',
            new_name='descricao',
        ),
    ]
