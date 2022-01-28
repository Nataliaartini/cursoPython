class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f"{self.nomeclasse} falando")

class Cliente(Pessoa):
    def comprar(self):
        print(f"{self.nomeclasse} comprando")


class Aluno(Pessoa):
    def estudar(self):
        print(f"{self.nomeclasse} estudando")


cliente1 = Cliente("Amanda", 18)
print(cliente1.nome)
cliente1.comprar()
aluno1 = Aluno("Jonas", 26)
print(aluno1.nome)
aluno1.falar()
