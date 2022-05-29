import collections

from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.urls import reverse
from matplotlib import pyplot as plt

from portfolio.models import Cadeira, Projeto, Escola, Interesse, Pessoa, Linguagen, Tecnologia, Laboratorio, Noticia, \
    PontuacaoQuizz, resolution_path, BlogPost


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


def sobreestewebsite_page_view(request):
    return render(request, 'portfolio/sobreestewebsite.html')


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

        if collections.Counter(request.POST.getlist("linguagem[]")) == collections.Counter(
                ("css", "html", "javascript")):
            p = p + 1

        if request.POST["opcao"] == "img":
            p = p + 1

        if request.POST["datecriacao"] == "2005-07-21":
            p = p + 1

        if request.POST["pagecolor"] == "#ffffff":
            p = p + 1

        if request.POST["launchYear"] == "1993":
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
    return render(request, 'portfolio/educacao.html', {"escolas": Escola.objects.all()})


def certificados_page_view(request):
    return render(request, 'portfolio/certificados.html')


def outrashabilitacoes_page_view(request):
    return render(request, 'portfolio/outrashabilitacoes.html')


def aptidoesecompetencias_page_view(request):
    return render(request, 'portfolio/aptidoesecompetencias.html')


def interessesehobbies_page_view(request):
    return render(request, 'portfolio/interessesehobbies.html', {"interesses": Interesse.objects.all()})


def tfcs_page_view(request):
    return render(request, 'portfolio/tfcs.html')


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
            return HttpResponseRedirect(reverse('portfolio:lista'))
        else:
            return render(request, 'portfolio/login.html', {
                'message': 'Credenciais invalidas.'
            })

    return render(request, 'portfolio/login.html')
