from django.db import models

# Create your models here.

class Book(models.Model):
    nome = models.CharField(max_length=50,unique=True)
    descricao = models.CharField(max_length=100)
    nota = models.IntegerField()

    def __str__(self):
        return self.nome

    