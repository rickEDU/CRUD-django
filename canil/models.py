from django.db import models

class Cao(models.Model):
    nome = models.CharField(max_length=20)
    raca = models.CharField(max_length=20)
    idade = models.IntegerField()

    def __str__(self):
        return self.nome