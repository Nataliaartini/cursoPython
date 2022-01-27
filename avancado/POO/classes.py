import datetime
import random as rd
class Pessoa:
    print("\n")
    ano_atual = int(datetime.datetime.strftime(datetime.datetime.now(), "%Y"))
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self, alimento):
        if self.comendo:
            print(f"{self.nome} já está comendo")
            return
        if self.falando:
            print(f"{self.nome} está falando agora e não pode comer")
            return
        print(f"{self.nome} está comendo {alimento}.")
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(F"{self.nome} não está comendo.")
            return
        print(f"{self.nome} parou de comer.")
        self.comendo = False

    def falar(self, assunto):
        if self.comendo:
            print(f"{self.nome} está comendo agora e não pode falar")
            return
        if self.falando:
            print(f"{self.nome} já está falando.")
            return
        print(f"{self.nome} está falando sobre {assunto}.")
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f"{self.nome} não está falando")
            return
        print(f"{self.nome} parou de falar.")
        self.falando = False

    def nascimento(self):
        return self.ano_atual - self.idade

    @classmethod
    def por_ano_nasc(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        rand = rd.randint(10000, 19999)
        return rand


p1 = Pessoa("Natalia", 21)
p2 = Pessoa("Anna", 20)
p3 = Pessoa.por_ano_nasc("Lucia", 1972)
print(f"{p1.nome} Id: {p1.gera_id()}")
print(f"{p2.nome} Id: {p2.gera_id()}")
print(f"{p3.nome} Id: {p3.gera_id()}")
print(p3.nome, p3.idade)
p3.nascimento()
print(f"Ano: {Pessoa.ano_atual}")

print(45*"*")
p1.falar("POO")
p1.comer("macarrão")
p1.parar_comer()
p1.parar_falar()
p1.comer("macarrão")
p1.falar("POO")
p1.comer("macarrão")
p1.parar_comer()
p1.falar("POO")
print(45*"*")
p2.falar("BBB")
p2.parar_comer()
p2.parar_falar()
p2.comer("alface")
p2.comer("geleia")
print(p2.nascimento())
