from django.shortcuts import render
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "portfolio"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('licenciatura', views.licenciatura_page_view, name='licenciatura'),
    path('licenciatura_nova_cadeira', views.licenciatura_nova_cadeira_view, name='licenciatura_nova_cadeira'),
    path('licenciatura_edita_cadeira/<int:cadeira_id>', views.licenciatura_edita_cadeira_view, name='licenciatura_edita_cadeira'),
    path('licenciatura_apaga_cadeira/<int:cadeira_id>', views.licenciatura_apaga_cadeira_view, name='licenciatura_apaga_cadeira'),

    path('aptidoes', views.aptidoesecompetencias_page_view, name='aptidoes'),
    path('nova_aptidao', views.nova_aptidao_view, name='nova_aptidao'),
    path('edita_aptidao/<int:aptidao_id>', views.edita_aptidao_view, name='edita_aptidao'),
    path('apaga_aptidao/<int:aptidao_id>', views.apaga_aptidao_view, name='apaga_aptidao'),

    path('projetos', views.projetos_page_view, name='projetos'),
    path('novo_projeto', views.novo_projeto_view, name='novo_projeto'),
    path('edita_projeto/<int:projeto_id>', views.edita_projeto_view, name='edita_projeto'),
    path('apaga_projeto/<int:projeto_id>', views.apaga_projeto_view, name='apaga_projeto'),

    path('programacaowebtecnologias', views.programacaowebtecnologias_page_view, name='programacaowebtecnologias'),
    path('nova_tecnologia', views.nova_tecnologia_view, name='nova_tecnologia'),
    path('edita_tecnologia/<int:tecnologia_id>', views.edita_tecnologia_view, name='edita_tecnologia'),
    path('apaga_tecnologia/<int:tecnologia_id>', views.apaga_tecnologia_view, name='apaga_tecnologia'),

    path('blog', views.blog_page_view, name='blog'),
    path('novo_post', views.novo_post_view, name='novo_post'),
    path('edita_post/<int:post_id>', views.edita_post_view, name='edita_post'),
    path('apaga_post/<int:post_id>', views.apaga_post_view, name='apaga_post'),

    path('contactos', views.contactos_page_view, name='contactos'),

    path('laboratorios', views.laboratorios_page_view, name='laboratorios'),
    path('novo_laboratorio', views.novo_laboratorio_view, name='novo_laboratorio'),
    path('edita_laboratorio/<int:laboratorio_id>', views.edita_laboratorio_view, name='edita_laboratorio'),
    path('apaga_laboratorio/<int:laboratorio_id>', views.apaga_laboratorio_view, name='apaga_laboratorio'),

    path('noticias', views.noticias_page_view, name='noticias'),
    path('nova_noticia', views.nova_noticia_view, name='nova_noticia'),
    path('edita_noticia/<int:noticia_id>', views.edita_noticia_view, name='edita_noticia'),
    path('apaga_noticia/<int:noticia_id>', views.apaga_noticia_view, name='apaga_noticia'),

    path('exemplosetecnicas', views.exemplosetecnicas_page_view, name='exemplosetecnicas'),

    path('quizz', views.quizz_page_view, name='quizz'),

    path('educacao', views.educacao_page_view, name='educacao'),
    path('nova_escola', views.nova_escola_view, name='nova_escola'),
    path('edita_escola/<int:escola_id>', views.edita_escola_view, name='edita_escola'),
    path('apaga_escola/<int:escola_id>', views.apaga_escola_view, name='apaga_escola'),

    path('certificados', views.certificados_page_view, name='certificados'),

    path('outrashabilitacoes', views.outrashabilitacoes_page_view, name='outrashabilitacoes'),

    path('aptidoesecompetencias', views.aptidoesecompetencias_page_view, name='aptidoesecompetencias'),

    path('interessesehobbies', views.interessesehobbies_page_view, name='interessesehobbies'),

    path('novo_interesse', views.novo_interesse_view, name='novo_interesse'),
    path('edita_interesse/<int:interesse_id>', views.edita_interesse_view, name='edita_interesse'),
    path('apaga_interesse/<int:interesse_id>', views.apaga_interesse_view, name='apaga_interesse'),

    path('tfcs', views.tfcs_page_view, name='tfcs'),
    path('novo_tfc', views.novo_tfc_view, name='novo_tfc'),
    path('edita_tfc/<int:tfc_id>', views.edita_tfc_view, name='edita_tfc'),
    path('apaga_tfc/<int:tfc_id>', views.apaga_tfc_view, name='apaga_tfc'),

    path('login/', views.login_page_view, name='login'),
    path('logout/', views.logout_page_view, name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
