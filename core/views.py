from django.shortcuts import render
from portfolio.models import Proyecto
def home(request):
    return render(request, template_name="core/home.html")

def about(request):
    return render(request, template_name="core/about.html")

def portafolio(request):
    # Aquí pedimos todos los proyectos que subiste al admin
    proyectos = Proyecto.objects.all()
    return render(request, "core/Portafolio.html", {'proyectos': proyectos})

def contacto(request):
    return render(request, template_name="core/Contacto.html")