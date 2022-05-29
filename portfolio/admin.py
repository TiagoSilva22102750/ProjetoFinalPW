from django.contrib import admin

# Register your models here.
from portfolio.models import Pessoa, Projeto, Cadeira, Linguagen, Escola, Interesse, Tecnologia, Laboratorio, Noticia


class PessoaAdmin(admin.ModelAdmin):
    fields = ("nome", "linkDaPessoaLusofona", "linkDaPessoaLinkedIn", "linkPortfolioPW")


admin.site.register(Pessoa, PessoaAdmin)


class LinguagenAdmin(admin.ModelAdmin):
    fields = ("nome",)


admin.site.register(Linguagen, LinguagenAdmin)


class ProjetoAdmin(admin.ModelAdmin):
    fields = ("nome", "descricao", "linguagemUtilizada", "anoLetivoEmQueFoiRealizado", "participantes", "linkGitHub",
              "linkVideoYoutube")


admin.site.register(Projeto, ProjetoAdmin)


class CadeiraAdmin(admin.ModelAdmin):
    fields = ("nome", "ano", "semestre", "anoLetivoFrequentado", "ects", "descricao", "linguagens", "docente_teorica",
              "docente_praticas", "projetos", "rating", "urlCadeira")


admin.site.register(Cadeira, CadeiraAdmin)


class EscolaAdmin(admin.ModelAdmin):
    fields = ("nome", "local", "cursoFrequentado", "periodoNaInstituicao", "imagem")


admin.site.register(Escola, EscolaAdmin)


class InteresseAdmin(admin.ModelAdmin):
    fields = ("titulo", "descricao", "link")


admin.site.register(Interesse, InteresseAdmin)


class TecnologiaAdmin(admin.ModelAdmin):
    fields = ("nomeExtenso", "sigla", "anoDeCriacao", "criador", "linkSiteOficial", "descricao")


admin.site.register(Tecnologia, TecnologiaAdmin)


class LaboratorioAdmin(admin.ModelAdmin):
    fields = ("titulo", "descricao", "link")


admin.site.register(Laboratorio, LaboratorioAdmin)


class NoticiaAdmin(admin.ModelAdmin):
    fields = ("titulo", "texto", "linkNoticia")


admin.site.register(Noticia, NoticiaAdmin)