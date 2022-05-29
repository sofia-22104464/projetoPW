from django.urls import path, include

from portfolio import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home),
    path('home', views.home, name='home'),
    path('presentation', views.presentation, name='presentation'),
    path('formation', views.formation, name='formation'),
    path('projects', views.projects, name='projects'),
    path('skills', views.skills, name='skills'),
]
