
from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


#valida o input de entra, aceitando pelas letras
alphanumeric = RegexValidator(r'^[a-zA-Z ]*$','Only letters are allowed')

class Modalidade(models.Model):
    ## nao eh necessario criar a chave primaria
    ## o django ja cria automaticamente

    def __unicode__(self):
        return u'{0}'.format(self.descricao)

    descricao = models.CharField(max_length=100,null = False,validators = [alphanumeric])


class Turno(models.Model):

    def __unicode__(self):
        return u'{0}'.format(self.descricao)

    descricao = models.CharField(max_length=100,null = False,validators = [alphanumeric])
    ## Pode-se usar o choice para escolher opcoes
    ## https://www.codementor.io/tips/7714213398/django-form-choices-loaded-from-database-are-not-updated


class Curso(models.Model):

    def __unicode__(self):
        return u'{0}'.format(self.descricao)

    descricao = models.CharField(max_length=100,null = False,validators = [alphanumeric])
    modalidade = models.ForeignKey(Modalidade)
    ## a chave estrangeira eh o nome da class in lower-case for default
                                             ## eh possivel criar uma variavel de referencia variave_ref = 'nome_ref'



class Aluno(models.Model):

    def __unicode__(self):
        return u'{0}'.format(self.nome)

    nome = models.CharField(max_length = 200,null = False,validators = [alphanumeric])
    curso = models.ForeignKey(Curso)
    turno = models.ForeignKey(Turno)

