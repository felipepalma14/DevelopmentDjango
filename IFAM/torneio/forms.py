# -*- coding: utf-8 -*-

from django import forms
from torneio.models import Modalidade, Turno, Curso, Aluno


class ModalidadeForm(forms.ModelForm):
    descricao = forms.CharField(label=u'Descrição',max_length=100)
    class Meta:
        model = Modalidade
        fields = ('descricao',)


class TurnoCursoForm(forms.ModelForm):
    descricao =forms.CharField(label=u'Descrição',max_length=100)
    class Meta:
        model = Turno
        fields = ('descricao',)


class CursoForm(forms.ModelForm):
    descricao = forms.CharField(label= u'Descrição',max_length=100)
    modalidade = forms.ModelChoiceField(label='Modalidade',queryset= Modalidade.objects.all())

    class Meta:
        model = Curso
        fields = ('descricao','modalidade',)

class AlunoForm(forms.ModelForm):
    nome = forms.CharField(label='Aluno',max_length=100)
    curso = forms.ModelChoiceField(label='Curso',queryset= Curso.objects.all())
    turno = forms.ModelChoiceField(label='Turno',queryset= Turno.objects.all())
    

    class Meta:
        model = Aluno
        fields = ('nome','curso','turno')

