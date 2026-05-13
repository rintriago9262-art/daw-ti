from django.contrib import admin
from portfolio.models import Proyecto

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha_creacion', 'fecha_modificacion']
    readonly_fields = ['fecha_creacion', 'fecha_modificacion']