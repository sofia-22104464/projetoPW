from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, "portfolio/home.html")


def presentation(request):
    return render(request, "portfolio/presentation.html")


def formation(request):
    return render(request, "portfolio/formation.html")


def projects(request):
    return render(request, "portfolio/projects.html")


def skills(request):
    return render(request, "portfolio/skills.html")
