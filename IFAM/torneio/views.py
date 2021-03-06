from django.shortcuts import render, render_to_response, redirect, get_object_or_404

# Create your views here.
from django.template import RequestContext
from ifam import settings
from torneio.forms import ModalidadeForm, TurnoCursoForm, CursoForm, AlunoForm
from torneio.models import Modalidade, Aluno, Curso, Turno
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login



def login_user(request):
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username,password = password)

        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect('/listarcursos')
    return render_to_response("login.html",{}, 
        context_instance = RequestContext(request))

def logout(request):
    logout(request)
    return render_to_response('logout.html')
def menu(request):
    return render_to_response("base.html",{'MEDIA_URL':settings.MEDIA_URL},
        context_instance = RequestContext(request))

def listarAlunos(request):
    all_alunos = Aluno.objects.all().order_by('nome')# ordena por nome
    turno_aluno = Curso.objects.all()
    return render_to_response("listaaluno.html",{'all_alunos': all_alunos,
                                                 'MEDIA_URL':settings.MEDIA_URL,'turno_aluno':turno_aluno},
                              context_instance = RequestContext(request))

def excluirAluno(request,nr_aluno):
    all_alunos = get_object_or_404(Aluno,pk=nr_aluno)
    if request.method == 'POST':
        all_alunos.delete()
        return redirect('/listaraluno')
    return render(request,'deletaaluno.html',{'all_alunos':all_alunos},
    context_instance = RequestContext(request))

def listarModalidades(request):
    #return HttpResponse('Hello Word!!')
    all_modalidade = Modalidade.objects.all()
    return render_to_response("listamodalidade.html",{'all_modalidade': all_modalidade,
                                                      'MEDIA_URL':settings.MEDIA_URL},
                              context_instance = RequestContext(request))


def adicionarModalidade(request):
    form = ModalidadeForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/listarmodalidade')

    return render(request,'adicionarmodalidade.html',{'form':form})

def excluirModalidade(request,nr_modalidade):
    all_modalidade = get_object_or_404(Modalidade,pk=nr_modalidade)
    if request.method == 'POST':
        all_modalidade.delete()
        return redirect('/listarmodalidade')
    return render(request,"deletamodalidade.html",{'all_modalidade':all_modalidade})

def adicionarTurno(request):
    form = TurnoCursoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/listarturnos')
    return render(request,"adicionaturno.html",{'form':form})

def listarTurno(request):
    all_turnos = Turno.objects.all()
    return render_to_response('listarturno.html',{'all_turnos':all_turnos,
                                                  'MEDIA_URL':settings.MEDIA_URL},
                              context_instance= RequestContext(request))
def excluirTurno(request,nr_turno):
    all_turno = get_object_or_404(Turno,pk=nr_turno)
    if request.method == 'POST':
        all_turno.delete()
        return redirect('/listarturnos')
    return render_to_response('deletaturno.html',{'all_turno':all_turno},
        context_instance = RequestContext(request))

def adicionarCurso(request):
    form = CursoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/listarcursos')
    return render(request,"adicionacurso.html",{'form':form})

def listarCursos(request):
    all_cursos = Curso.objects.all()
    return render_to_response("listarcurso.html",{'all_cursos': all_cursos,
                                                      'MEDIA_URL':settings.MEDIA_URL},
                              context_instance = RequestContext(request))
def excluirCurso(request,nr_curso):
    all_curso = get_object_or_404(Curso,pk=nr_curso)
    if request.method == 'POST':
        all_curso.delete()
        return redirect('/listarcursos')
    return render_to_response('deletacurso.html',{'all_curso':all_curso },context_instance = RequestContext(request))


def adicionarAluno(request):
    form = AlunoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/listaraluno')
    return render(request,"adicionaaluno.html",{'form':form})

