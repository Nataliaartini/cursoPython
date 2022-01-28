class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def insere_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))

    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)

    def __del__(self):
        print(f"{self.nome} foi excluído")

class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print(f"{self.cidade}/{self.estado} foi excluído")


cliente1 = Cliente("Amanda", 18)
cliente1.insere_endereco("Florianópolis", "SC")
print(cliente1.nome)
cliente1.lista_enderecos()
del cliente1
print(45*"*")
cliente2 = Cliente("Jonas", 26)
cliente2.insere_endereco("Chapecó", "SC")
cliente2.insere_endereco("São Paulo", "SP")
print(cliente2.nome)
cliente2.lista_enderecos()
del cliente2 #sem o del o garbage colector do python apaga esses dados ao final da execução
print(45*"*")
