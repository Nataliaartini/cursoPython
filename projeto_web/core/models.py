from django.db import models


class Produto(models.Model):
    nome = models.CharField("Nome", max_length=100)
    preco = models.FloatField("Preco")
    estoque = models.IntegerField("estoque inteiro apenas")


class Cliente(models.Model):
    nome = models.CharField("Nome", max_length=50)
    sobrenome = models.CharField("Sobrenome", max_length=100)
    email = models.EmailField("E-mail", max_length=100)
