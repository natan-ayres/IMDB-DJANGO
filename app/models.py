from django.db import models

class Filmes(models.Model):
    nome = models.CharField(max_length=30)
    desc = models.TextField(max_length=70)
    data = models.DateField()
    nota_media = models.FloatField()
    reviews = models.TextField(max_length=150)
    def __str__(self):
        return f'{self.nome}'
    






