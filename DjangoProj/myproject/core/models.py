from django.db import models


class Jogo(models.Model):
    nome = models.TextField(max_length=23)
    valor = models.DecimalField(decimal_places=2, max_digits=7)

    def __str__(self):
        return self.nome

