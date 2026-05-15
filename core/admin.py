from django.contrib import admin
from core.models import Persona

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ['nombres', 'apellidos', 'correo', 'titulo_academico']