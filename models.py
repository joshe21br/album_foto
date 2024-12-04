# galeria/models.py
from django.db import models

class Foto(models.Model):
    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='fotos/')
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titulo
