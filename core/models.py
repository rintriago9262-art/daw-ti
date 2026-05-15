from django.db import models

class Persona(models.Model):
    nombres = models.CharField(max_length=100, verbose_name="Nombres")
    apellidos = models.CharField(max_length=100, verbose_name="Apellidos")
    direccion = models.CharField(max_length=200, verbose_name="Dirección")
    telefono = models.CharField(max_length=20, verbose_name="Teléfono")
    titulo_academico = models.CharField(max_length=200, verbose_name="Título Académico")
    biografia = models.TextField(verbose_name="Biografía")
    correo = models.EmailField(verbose_name="Correo Electrónico")
    dedicacion = models.CharField(max_length=200, verbose_name="Dedicación")

    class Meta:
        verbose_name = "persona"
        verbose_name_plural = "personas"

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"