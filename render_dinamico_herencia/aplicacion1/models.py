from django.db import models

class Publicacion(models.Model):
    titulo = models.CharField(max_length=120)
    resumen = models.CharField(max_length=220)
    contenido = models.TextField()
    publicado = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)
