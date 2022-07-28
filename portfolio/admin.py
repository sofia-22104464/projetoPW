from django.contrib import admin

# Register your models here.
from portfolio.models import Pessoa, Projeto, Cadeira, AptidoesECompetencia, Linguagen, Escola, Interesse, Tecnologia, \
    Laboratorio, Noticia, \
    PontuacaoQuizz, BlogPost, TFC


class PessoaAdmin(admin.ModelAdmin):
    fields = ("nome", "linkDaPessoaLusofona", "linkDaPessoaLinkedIn", "linkPortfolioPW")


admin.site.register(Pessoa, PessoaAdmin)


class LinguagenAdmin(admin.ModelAdmin):
    fields = ("nome",)


admin.site.register(Linguagen, LinguagenAdmin)


class ProjetoAdmin(admin.ModelAdmin):
    fields = ("nome", "descricao", "imagem", "linguagemUtilizada", "anoLetivoEmQueFoiRealizado", "participantes",
              "linkGitHub", "linkVideoYoutube")


admin.site.register(Projeto, ProjetoAdmin)


class CadeiraAdmin(admin.ModelAdmin):
    fields = ("nome", "ano", "semestre", "anoLetivoFrequentado", "ects", "descricao", "linguagens", "docente_teorica",
              "docente_praticas", "projetos", "rating", "urlCadeira")


admin.site.register(Cadeira, CadeiraAdmin)


class AptidoesECompetenciaAdmin(admin.ModelAdmin):
    fields = ("titulo", "descricaoCurta", "listaProjetos", "listaDisciplinas")


admin.site.register(AptidoesECompetencia, AptidoesECompetenciaAdmin)


class EscolaAdmin(admin.ModelAdmin):
    fields = ("nome", "local", "cursoFrequentado", "periodoNaInstituicao", "imagem")


admin.site.register(Escola, EscolaAdmin)


class InteresseAdmin(admin.ModelAdmin):
    fields = ("titulo", "descricao", "imagem", "link")


admin.site.register(Interesse, InteresseAdmin)


class TecnologiaAdmin(admin.ModelAdmin):
    fields = ("nomeExtenso", "sigla", "tipo", "anoDeCriacao", "criador", "linkSiteOficial", "descricao", "imagem")


admin.site.register(Tecnologia, TecnologiaAdmin)


class LaboratorioAdmin(admin.ModelAdmin):
    fields = ("titulo", "descricao", "link")


admin.site.register(Laboratorio, LaboratorioAdmin)


class NoticiaAdmin(admin.ModelAdmin):
    fields = ("titulo", "texto", "linkNoticia", "imagem")


admin.site.register(Noticia, NoticiaAdmin)


class PontuacaoQuizzAdmin(admin.ModelAdmin):
    fields = ("nome", "pontuacao")


admin.site.register(PontuacaoQuizz, PontuacaoQuizzAdmin)


class BlogPostAdmin(admin.ModelAdmin):
    fields = ("autor", "data", "titulo", "descricao", "urlProjetoOuPortfolio", "imagem")


admin.site.register(BlogPost, BlogPostAdmin)


class TFCAdmin(admin.ModelAdmin):
    fields = ("autores", "orientadores", "ano", "titulo", "resumo", "imagem", "urlRelatorio", "urlGitHub", "urlYouTube")


admin.site.register(TFC, TFCAdmin)
