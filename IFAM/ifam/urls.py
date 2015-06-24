
"""ifam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'torneio.views.menu'),
    # URL`s ADD
    url(r'^adicionarmodalidade/$','torneio.views.adicionarModalidade'),
    url(r'^adicionarturno/$','torneio.views.adicionarTurno'),
    url(r'^adicionarcurso/$','torneio.views.adicionarCurso'),
    url(r'^adicionaraluno/$','torneio.views.adicionarAluno'),

    url(r'^listarcursos/$','torneio.views.listarCursos'),
    url(r'^listarmodalidade/$','torneio.views.listarModalidades'),
    url(r'^listaraluno/$','torneio.views.listarAlunos'),
    url(r'^listarturnos/$','torneio.views.listarTurno'),

    url(r'^excluirmodalidade/(?P<nr_modalidade>\d+)/$','torneio.views.excluirModalidade'),
    url(r'^excluiraluno/(?P<nr_aluno>\d+)/$','torneio.views.excluirAluno'),
    url(r'^excluirturno/(?P<nr_turno>\d+)/$','torneio.views.excluirTurno'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



if settings.DEBUG:
    urlpatterns += patterns('',
                            (r'^media/(?P<path>.*)$','django.views.static.serve',
         {'document_root':settings.MEDIA_ROOT}),)
