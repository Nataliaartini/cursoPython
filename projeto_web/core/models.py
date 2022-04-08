from django.db import models


class Produto(models.Model):
    nome = models.CharField("Nome", max_length=100)
    preco = models.FloatField("Preco")
    estoque = models.IntegerField("estoque inteiro apenas")
    descricao = models.TextField("Descrição", blank=True, null=True)

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField("Nome", max_length=50)
    sobrenome = models.CharField("Sobrenome", max_length=100)
    email = models.EmailField("E-mail", max_length=100)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
