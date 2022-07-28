from django.forms import ModelForm
from django import forms

from portfolio.models import Cadeira, Projeto, Tecnologia, Noticia, Laboratorio, Interesse, Escola, BlogPost, \
    AptidoesECompetencia, TFC


class CadeiraForm(ModelForm):
    descricao = forms.CharField(widget=forms.Textarea(attrs={"rows": 3}))

    class Meta:
        model = Cadeira
        fields = '__all__'


class AptidoesECompetenciaForm(ModelForm):
    descricao = forms.CharField(widget=forms.Textarea(attrs={"rows": 3}))

    class Meta:
        model = AptidoesECompetencia
        fields = '__all__'


class ProjetoForm(ModelForm):
    descricao = forms.CharField(widget=forms.Textarea(attrs={"rows": 3}))

    class Meta:
        model = Projeto
        fields = '__all__'


class TecnologiaForm(ModelForm):
    descricao = forms.CharField(widget=forms.Textarea(attrs={"rows": 3}))

    class Meta:
        model = Tecnologia
        fields = '__all__'


class NoticiaForm(ModelForm):
    descricao = forms.CharField(widget=forms.Textarea(attrs={"rows": 3}))

    class Meta:
        model = Noticia
        fields = '__all__'


class LaboratorioForm(ModelForm):
    descricao = forms.CharField(widget=forms.Textarea(attrs={"rows": 3}))

    class Meta:
        model = Laboratorio
        fields = '__all__'


class InteresseForm(ModelForm):
    descricao = forms.CharField(widget=forms.Textarea(attrs={"rows": 3}))

    class Meta:
        model = Interesse
        fields = '__all__'


class EscolaForm(ModelForm):
    descricao = forms.CharField(widget=forms.Textarea(attrs={"rows": 3}))

    class Meta:
        model = Escola
        fields = '__all__'


class BlogPostForm(ModelForm):
    descricao = forms.CharField(widget=forms.Textarea(attrs={"rows": 3}))

    class Meta:
        model = BlogPost
        fields = '__all__'


class TFCForm(ModelForm):
    descricao = forms.CharField(widget=forms.Textarea(attrs={"rows": 3}))

    class Meta:
        model = TFC
        fields = '__all__'
