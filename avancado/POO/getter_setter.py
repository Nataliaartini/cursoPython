class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()

    # getter
    @property
    def preco(self):
        return self._preco

    # setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace("R$", ""))
        self._preco = valor


p1 = Produto("cd calcinha preta", "R$10")
p1.desconto(50)
print(p1.nome, p1.preco)

p2 = Produto("traduzindo sonhos pro jogo do bicho", 30)
p2.desconto(5)
print(p2.nome, p2.preco)


class Pessoa:
    def __init__(self, nome):
        self._nome = nome  # esse atributo só serve pra salvar o valor utilizado no setter e getter

    @property
    def nome(self):
        return self._nome  # com o atributo

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def sobrenome(self):
        return "Pereira"


p1 = Pessoa("Bernardino")
# p1.nome = "ricardo" #vai mudar o valor de atributo na def init
print(p1.nome)  # continua com o valor do setter enquanto o return de property nao tiver atributo
print(p1.sobrenome)
