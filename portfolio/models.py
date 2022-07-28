from django.db import models


# Create your models here.

def resolution_path(instance, filename):
    return f'users/{instance.id}'


class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    linkDaPessoaLusofona = models.URLField(default="", null=True, blank=True)
    linkDaPessoaLinkedIn = models.URLField(default="", null=True, blank=True)
    linkPortfolioPW = models.URLField(default="", null=True, blank=True)

    def __str__(self):
        return self.nome


class Linguagen(models.Model):
    nome = models.CharField(max_length=15)

    def __str__(self):
        return self.nome


class Projeto(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(max_length=500)
    imagem = models.ImageField(upload_to=resolution_path, blank=True)
    linguagemUtilizada = models.ManyToManyField(Linguagen, related_name='linguagemUsada')
    anoLetivoEmQueFoiRealizado = models.CharField(default="2020/21", max_length=15, null=True, blank=True)
    participantes = models.ManyToManyField(Pessoa, null=True, blank=True, related_name='participantes')
    linkGitHub = models.URLField(default="", null=True, blank=True)
    linkVideoYoutube = models.URLField(default="", null=True, blank=True)

    def __str__(self):
        return self.nome


class Cadeira(models.Model):
    nome = models.CharField(max_length=57)
    ano = models.IntegerField(choices=[(1, 1), (2, 2), (3, 3)])
    semestre = models.IntegerField(choices=[(1, 1), (2, 2)], default=1)
    anoLetivoFrequentado = models.CharField(max_length=15)
    ects = models.IntegerField(default=1)
    descricao = models.TextField()
    linguagens = models.ManyToManyField(Linguagen, related_name='linguagem')
    docente_teorica = models.ManyToManyField(Pessoa, related_name='teoricas')
    docente_praticas = models.ManyToManyField(Pessoa, related_name='praticas')
    projetos = models.ManyToManyField(Projeto, null=True, blank=True, related_name='projeto')
    rating = models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=3)
    urlCadeira = models.URLField(default="", null=True, blank=True)

    def __str__(self):
        return self.nome


class AptidoesECompetencia(models.Model):
    titulo = models.CharField(max_length=75)
    descricaoCurta = models.TextField(max_length=250)
    listaProjetos = models.ManyToManyField(Projeto, related_name='projetos', null=True, blank=True)
    listaDisciplinas = models.ManyToManyField(Cadeira, related_name="disciplinas", null=True, blank=True)

    def __str__(self):
        return self.titulo


class Escola(models.Model):
    nome = models.CharField(max_length=57)
    local = models.CharField(max_length=20)
    cursoFrequentado = models.CharField(max_length=31)
    periodoNaInstituicao = models.CharField(max_length=15)
    imagem = models.ImageField(upload_to=resolution_path, blank=True)

    def __str__(self):
        return self.nome


class Interesse(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to=resolution_path, blank=True)
    link = models.URLField(default="", null=True, blank=True)

    def __str__(self):
        return self.titulo


class Tecnologia(models.Model):
    nomeExtenso = models.CharField(max_length=75)
    sigla = models.CharField(max_length=10)
    tipo = models.CharField(max_length=31, default="")
    anoDeCriacao = models.IntegerField()
    criador = models.CharField(max_length=115)
    linkSiteOficial = models.URLField(default="", null=True, blank=True)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to=resolution_path, blank=True, null=True)

    def __str__(self):
        return self.sigla


class Laboratorio(models.Model):
    titulo = models.CharField(max_length=75)
    descricao = models.TextField()
    link = models.URLField(default="", null=True, blank=True)

    def __str__(self):
        return self.titulo


class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    linkNoticia = models.URLField(default="", null=True, blank=True)
    imagem = models.ImageField(upload_to=resolution_path, blank=True)

    def __str__(self):
        return self.titulo


class PontuacaoQuizz(models.Model):
    nome = models.CharField(max_length=50)
    pontuacao = models.IntegerField()

    def __str__(self):
        return self.nome


class BlogPost(models.Model):
    autor = models.CharField(max_length=50)
    data = models.DateField(default="2022-06-12")
    titulo = models.CharField(max_length=75)
    descricao = models.TextField()
    urlProjetoOuPortfolio = models.URLField(default="", null=True, blank=True)
    imagem = models.ImageField(upload_to=resolution_path, blank=True, null=True)

    def __str__(self):
        return self.titulo


class TFC(models.Model):
    autores = models.CharField(max_length=150)
    orientadores = models.CharField(max_length=150)
    ano = models.CharField(max_length=4)
    titulo = models.CharField(max_length=75)
    resumo = models.TextField()
    imagem = models.ImageField(upload_to=resolution_path, blank=True, null=True)
    urlRelatorio = models.URLField(default="", null=True, blank=True)
    urlGitHub = models.URLField(default="", null=True, blank=True)
    urlYouTube = models.URLField(default="", null=True, blank=True)

    def __str__(self):
        return self.titulo
