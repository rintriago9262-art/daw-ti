from django.db import models

class Proyecto(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título del Proyecto")
    descripcion = models.TextField(verbose_name="Descripción")
    imagen = models.ImageField(upload_to="proyectos", verbose_name="Imagen")
    enlace = models.URLField(null=True, blank=True, verbose_name="Enlace externo (Opcional)")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-fecha_creacion"]

    def __str__(self):
        return self.titulo