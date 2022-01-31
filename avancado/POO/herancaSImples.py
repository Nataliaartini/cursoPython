"""existem animais, eles respiram, é o topo da herança
        o lobo é um animal, então ele herda a funcao de respirar, ele tambem uiva
            o cachorro fica abaixo de lobo na herança, ele é animal, logo respira, e herda o uivo do lobo, e ele late
    este é um exemplo de como funciona herança"""
#um pai pode herdar de um filho, porém não é muito bom fazer isso, deixa o código mais complexo

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
print(45*"#")

class Biblioteca:
    def chama_metodo_da_interface(self):
        self.chama_metodo_da_interface() #um pai não deve herdar do filho...se executar isso aqui dentro vai gerar loop

class Interface(Biblioteca):
    def metodo_da_interface(self):
        print("sou metodo da interface")


i1 = Interface()
i1.metodo_da_interface()
#i1.chama_metodo_da_interface() seria o metodo da biblioteca herdado do seu filho interface
