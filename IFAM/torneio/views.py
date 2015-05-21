from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect, get_object_or_404

# Create your views here.
from torneio.forms import ModalidadeForm, TurnoCursoForm, CursoForm, AlunoForm
from torneio.models import Modalidade



def index(request):
    #return HttpResponse('Hello Word!!')
    return render(request,'menu.html',{})

def adicionarModalidade(request):
    form = ModalidadeForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request,'cadastramodalidade.html',{'form':form})

def excluirModalidade(request,nr_modalidade):
    all_modalidade = get_object_or_404(Modalidade,pk=nr_modalidade)
    if request.method == 'POST':
        all_modalidade.delete()
        return redirect('/')
    return render(request,"deletamodalidade.html",{'all_modalidade':all_modalidade})

def adicionarTurno(request):
    form = TurnoCursoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"adicionaturnocurso.html",{'form':form})

def adicionarCurso(request):
    form = CursoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"adicionacurso.html",{'form':form})

def adicionarAluno(request):
    form = AlunoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"adicionaaluno.html",{'form':form})


def menu(request):
    all_modalidade = Modalidade.objects.all()
    return render(request,"listamodalidade.html",{'all_modalidade': all_modalidade})
