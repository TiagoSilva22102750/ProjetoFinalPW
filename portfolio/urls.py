from django.shortcuts import render
from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('licenciatura', views.licenciatura_page_view, name='licenciatura'),
    path('projetos', views.projetos_page_view, name='projetos'),
    path('programacaowebtecnologias', views.programacaowebtecnologias_page_view, name='programacaowebtecnologias'),
    path('blog', views.blog_page_view, name='blog'),
    path('sobreestewebsite', views.sobreestewebsite_page_view, name='sobreestewebsite'),
    path('contactos', views.contactos_page_view, name='contactos'),
    path('laboratorios', views.laboratorios_page_view, name='laboratorios'),
    path('noticias', views.noticias_page_view, name='noticias'),
    path('exemplosetecnicas', views.exemplosetecnicas_page_view, name='exemplosetecnicas'),
    path('quizz', views.quizz_page_view, name='quizz'),
    path('educacao', views.educacao_page_view, name='educacao'),
    path('certificados', views.certificados_page_view, name='certificados'),
    path('outrashabilitacoes', views.outrashabilitacoes_page_view, name='outrashabilitacoes'),
    path('aptidoesecompetencias', views.aptidoesecompetencias_page_view, name='aptidoesecompetencias'),
    path('interessesehobbies', views.interessesehobbies_page_view, name='interessesehobbies'),
    path('tfcs', views.tfcs_page_view, name='tfcs'),
    path('login', views.login_page_view, name='login'),
]
