import collections

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.urls import reverse
import matplotlib.pyplot as plt

from portfolio.forms import CadeiraForm, ProjetoForm, TecnologiaForm, NoticiaForm, LaboratorioForm, InteresseForm, \
    EscolaForm, BlogPostForm, AptidoesECompetenciaForm, TFCForm
from portfolio.models import Cadeira, Projeto, Escola, Interesse, Pessoa, Linguagen, Tecnologia, Laboratorio, Noticia, \
    PontuacaoQuizz, resolution_path, BlogPost, AptidoesECompetencia, TFC


def home_page_view(request):
    return render(request, 'portfolio/home.html')


def licenciatura_page_view(request):
    elementos = Cadeira.objects.all()

    for elemento in elementos:
        elemento.__dict__["professorPraticas"] = list(Pessoa.objects.filter(praticas__id=elemento.id))
        elemento.__dict__["professorTeoricas"] = list(Pessoa.objects.filter(teoricas__id=elemento.id))
        elemento.__dict__["linguagemUtilizada"] = list(Linguagen.objects.filter(linguagem__id=elemento.id))
        elemento.__dict__["projetoRealizado"] = list(Projeto.objects.filter(projeto__id=elemento.id))

    return render(request, 'portfolio/licenciatura.html', {"cadeiras": elementos})


def aptidoesecompetencias_page_view(request):
    elementos = AptidoesECompetencia.objects.all()

    for elemento in elementos:
        elemento.__dict__["projetoRealizado"] = list(Projeto.objects.filter(projetos__id=elemento.id))
        elemento.__dict__["cadeiras"] = list(Cadeira.objects.filter(disciplinas__id=elemento.id))

    return render(request, 'portfolio/aptidoesecompetencias.html', {"aptidoes": elementos})


def projetos_page_view(request):
    elementos = Projeto.objects.all()

    for elemento in elementos:
        elemento.__dict__["linguagemUsada"] = list(Linguagen.objects.filter(linguagemUsada__id=elemento.id))
        elemento.__dict__["autores"] = list(Pessoa.objects.filter(participantes__id=elemento.id))

    return render(request, 'portfolio/projetos.html', {"projetos": elementos})


def programacaowebtecnologias_page_view(request):
    elementos = Tecnologia.objects.all()

    return render(request, 'portfolio/programacaowebtecnologias.html', {"tecnologias": elementos})


def blog_page_view(request):
    elementos = BlogPost.objects.all()

    return render(request, 'portfolio/blog.html', {"posts": elementos})


def contactos_page_view(request):
    return render(request, 'portfolio/contactos.html')


def laboratorios_page_view(request):
    elementos = Laboratorio.objects.all()

    return render(request, 'portfolio/laboratorios.html', {"laboratorios": elementos})


def noticias_page_view(request):
    elementos = Noticia.objects.all()

    return render(request, 'portfolio/noticias.html', {"noticias": elementos})


def exemplosetecnicas_page_view(request):
    return render(request, 'portfolio/exemplosetecnicas.html')


def quizz_page_view(request):
    if request.method == 'POST':
        n = request.POST['nome']
        p: int = 0

        try:
            elem = request.POST["elem"]
        except KeyError:
            elem = "head"
        if elem == "h1":
            p = p + 1

        try:
            opcao = request.POST["opcao"]
        except KeyError:
            opcao = "head"

        if opcao == "first":
            p = p + 1

        try:
            datecriacao = request.POST["elem"]
        except KeyError:
            datecriacao = "2004-07-21"

        if datecriacao == "2005-07-21":
            p = p + 1

        try:
            answer = request.POST["answer"]
        except KeyError:
            answer = "head"
        if answer.lower() == "cascade style sheet":
            p = p + 1

        r = PontuacaoQuizz(nome=n, pontuacao=p)
        r.save()

    languages_x = []
    popularity_y = []
    for pontuacao in PontuacaoQuizz.objects.all():
        languages_x.append(pontuacao.nome)
        popularity_y.append(pontuacao.pontuacao)

    languages_x.reverse()
    popularity_y.reverse()
    plt.barh(languages_x, popularity_y)
    plt.savefig('portfolio/static/portfolio/images/graph.png', bbox_inches='tight')
    plt.close()

    return render(request, 'portfolio/quizz.html')


def educacao_page_view(request):
    elementos1 = Escola.objects.all()
    return render(request, 'portfolio/educacao.html', {"escolas": elementos1})


def certificados_page_view(request):
    return render(request, 'portfolio/certificados.html')


def outrashabilitacoes_page_view(request):
    return render(request, 'portfolio/outrashabilitacoes.html')


def interessesehobbies_page_view(request):
    return render(request, 'portfolio/interessesehobbies.html', {"interesses": Interesse.objects.all()})


def tfcs_page_view(request):
    elementos = TFC.objects.all()

    return render(request, 'portfolio/tfcs.html', {"tfcs": elementos})


@login_required
def licenciatura_nova_cadeira_view(request):
    form = CadeiraForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:licenciatura'))

    context = {'form': form}

    return render(request, 'portfolio/novacadeira.html', context)


@login_required
def licenciatura_edita_cadeira_view(request, cadeira_id):
    cadeira = Cadeira.objects.get(pk=cadeira_id)
    form = CadeiraForm(request.POST or None, instance=cadeira)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:licenciatura'))

    context = {'form': form, 'cadeira_id': cadeira_id}

    return render(request, 'portfolio/editacadeira.html', context)


@login_required
def licenciatura_apaga_cadeira_view(request, cadeira_id):
    Cadeira.objects.get(pk=cadeira_id).delete()
    return HttpResponseRedirect(reverse('portfolio:licenciatura'))


@login_required
def nova_aptidao_view(request):
    form = AptidoesECompetenciaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:aptidoes'))

    context = {'form': form}

    return render(request, 'portfolio/novaaptidao.html', context)


@login_required
def edita_aptidao_view(request, aptidao_id):
    aptidao = AptidoesECompetencia.objects.get(pk=aptidao_id)
    form = AptidoesECompetenciaForm(request.POST or None, instance=aptidao)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:aptidoes'))

    context = {'form': form, 'aptidao_id': aptidao_id}

    return render(request, 'portfolio/editaaptidao.html', context)


@login_required
def apaga_aptidao_view(request, aptidao_id):
    AptidoesECompetencia.objects.get(pk=aptidao_id).delete()
    return HttpResponseRedirect(reverse('portfolio:aptidoes'))


@login_required
def novo_projeto_view(request):
    form = ProjetoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:projetos'))

    context = {'form': form}

    return render(request, 'portfolio/novoprojeto.html', context)


@login_required
def edita_projeto_view(request, projeto_id):
    projeto = Projeto.objects.get(pk=projeto_id)
    form = ProjetoForm(request.POST or None, instance=projeto)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:projetos'))

    context = {'form': form, 'projeto_id': projeto_id}

    return render(request, 'portfolio/editaprojeto.html', context)


@login_required
def apaga_projeto_view(request, projeto_id):
    Projeto.objects.get(pk=projeto_id).delete()
    return HttpResponseRedirect(reverse('portfolio:projetos'))


@login_required
def nova_tecnologia_view(request):
    form = TecnologiaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:programacaowebtecnologias'))

    context = {'form': form}

    return render(request, 'portfolio/novatecnologia.html', context)


@login_required
def edita_tecnologia_view(request, tecnologia_id):
    tecnologia = Tecnologia.objects.get(pk=tecnologia_id)
    form = TecnologiaForm(request.POST or None, instance=tecnologia)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:programacaowebtecnologias'))

    context = {'form': form, 'tecnologia_id': tecnologia_id}

    return render(request, 'portfolio/editatecnologia.html', context)


@login_required
def apaga_tecnologia_view(request, tecnologia_id):
    Tecnologia.objects.get(pk=tecnologia_id).delete()
    return HttpResponseRedirect(reverse('portfolio:programacaowebtecnologias'))


@login_required
def nova_noticia_view(request):
    form = NoticiaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:noticias'))

    context = {'form': form}

    return render(request, 'portfolio/novanoticia.html', context)


@login_required
def edita_noticia_view(request, noticia_id):
    noticia = Noticia.objects.get(pk=noticia_id)
    form = NoticiaForm(request.POST or None, instance=noticia)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:noticias'))

    context = {'form': form, 'noticia_id': noticia_id}

    return render(request, 'portfolio/editanoticia.html', context)


@login_required
def apaga_noticia_view(request, noticia_id):
    Noticia.objects.get(pk=noticia_id).delete()
    return HttpResponseRedirect(reverse('portfolio:noticias'))


@login_required
def novo_laboratorio_view(request):
    form = LaboratorioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:laboratorios'))

    context = {'form': form}

    return render(request, 'portfolio/novolaboratorio.html', context)


@login_required
def edita_laboratorio_view(request, laboratorio_id):
    laboratorio = Laboratorio.objects.get(pk=laboratorio_id)
    form = LaboratorioForm(request.POST or None, instance=laboratorio)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:laboratorios'))

    context = {'form': form, 'laboratorio_id': laboratorio_id}

    return render(request, 'portfolio/editalaboratorio.html', context)


@login_required
def apaga_laboratorio_view(request, laboratorio_id):
    Laboratorio.objects.get(pk=laboratorio_id).delete()
    return HttpResponseRedirect(reverse('portfolio:laboratorios'))


@login_required
def novo_interesse_view(request):
    form = InteresseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:interessesehobbies'))

    context = {'form': form}

    return render(request, 'portfolio/novointeresse.html', context)


@login_required
def edita_interesse_view(request, interesse_id):
    interesse = Interesse.objects.get(pk=interesse_id)
    form = InteresseForm(request.POST or None, instance=interesse)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:interessesehobbies'))

    context = {'form': form, 'interesse_id': interesse_id}

    return render(request, 'portfolio/editainteresse.html', context)


@login_required
def apaga_interesse_view(request, interesse_id):
    Interesse.objects.get(pk=interesse_id).delete()
    return HttpResponseRedirect(reverse('portfolio:interessesehobbies'))


@login_required
def nova_escola_view(request):
    form = EscolaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:educacao'))

    context = {'form': form}

    return render(request, 'portfolio/novaescola.html', context)


@login_required
def edita_escola_view(request, escola_id):
    escola = Escola.objects.get(pk=escola_id)
    form = EscolaForm(request.POST or None, instance=escola)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:educacao'))

    context = {'form': form, 'escola_id': escola_id}

    return render(request, 'portfolio/editaescola.html', context)


@login_required
def apaga_escola_view(request, escola_id):
    Escola.objects.get(pk=escola_id).delete()
    return HttpResponseRedirect(reverse('portfolio:educacao'))


def novo_post_view(request):
    form = BlogPostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form}

    return render(request, 'portfolio/novopost.html', context)


def edita_post_view(request, post_id):
    post = BlogPost.objects.get(pk=post_id)
    form = BlogPostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form, 'post_id': post_id}

    return render(request, 'portfolio/editapost.html', context)


def apaga_post_view(request, post_id):
    BlogPost.objects.get(pk=post_id).delete()
    return HttpResponseRedirect(reverse('portfolio:blog'))


@login_required
def novo_tfc_view(request):
    form = TFCForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:tfcs'))

    context = {'form': form}

    return render(request, 'portfolio/novotfc.html', context)


@login_required
def edita_tfc_view(request, tfc_id):
    tfc = TFC.objects.get(pk=tfc_id)
    form = TFCForm(request.POST or None, instance=tfc)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:tfcs'))

    context = {'form': form, 'tfc_id': tfc_id}

    return render(request, 'portfolio/editatfc.html', context)


@login_required
def apaga_tfc_view(request, tfc_id):
    TFC.objects.get(pk=tfc_id).delete()
    return HttpResponseRedirect(reverse('portfolio:tfcs'))


def login_page_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('portfolio:home'))
        else:
            return render(request, 'portfolio/login.html', {
                'message': 'Credenciais invalidas.'
            })

    return render(request, 'portfolio/login.html')


def logout_page_view(request):
    logout(request)

    return render(request, 'portfolio/home.html', {
        'message': 'Foi desconetado.'
    })
