# -*- coding: utf-8 -*-

from django import forms
from torneio.models import Modalidade, TurnoCurso, Curso, Aluno


class ModalidadeForm(forms.ModelForm):
    descricao = forms.CharField(label=u'Descrição',max_length=100)
    class Meta:
        model = Modalidade
        fields = ('descricao',)


class TurnoCursoForm(forms.ModelForm):
    descricao =forms.CharField(label=u'Descrição',max_length=100)
    class Meta:
        model = TurnoCurso
        fields = ('descricao',)


class CursoForm(forms.ModelForm):
    descricao = forms.CharField(label= u'Descrição',max_length=100)
    cursoModalidade = forms.ModelChoiceField(label='Modalidade',queryset= Modalidade.objects.all())
    cursoTurno = forms.ModelChoiceField(label='Turno',queryset= TurnoCurso.objects.all())
    class Meta:
        model = Curso
        fields = ('descricao','cursoModalidade','cursoTurno')

class AlunoForm(forms.ModelForm):
    nomeAluno = forms.CharField(label='Aluno',max_length=100)
    cursoAluno = forms.ModelChoiceField(label='Curso',queryset= Curso.objects.all())
    class Meta:
        model = Aluno
        fields = ('nomeAluno','cursoAluno')

