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


class ClienteVip(Cliente):
    def __init__(self, nome, sobrenome, idade):
        super().__init__(nome, idade)
        self.sobrenome = sobrenome

    def falar(self):
        super().falar()
        print(f"{self.nome} {self.sobrenome} está falando")


class Aluno(Pessoa):
    def estudar(self):
        print(f"{self.nomeclasse} estudando")


cliente1 = Cliente("Amanda", 18)
print(cliente1.nome)
cliente1.comprar()
print(28*"*")
aluno1 = Aluno("Jonas", 26)
print(aluno1.nome)
aluno1.falar()
print(28*"*")
clientvp = ClienteVip("Natalia", "Ferrandin", 21)
print(clientvp.nome)
clientvp.falar()
print(28*"*")
