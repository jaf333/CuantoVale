# En juego/models.py
from django.db import models

class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    valor_mercado = models.DecimalField(max_digits=10, decimal_places=2)
    imagen_url = models.URLField()

    def __str__(self):
        return self.nombre
