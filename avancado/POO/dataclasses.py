from dataclasses import dataclass #inicia com o def init, eq, repr, order, frozen, etc


@dataclass
class Pessoa:
    nome = str
    sobrenome = str

    def __post_init__(self):
        self.nome = f"{self.nome} {self.sobrenome}"

    def nome(self):
        return f"{self.nome} {self.sobrenome}"


p1 = Pessoa("Natalia", "Ferrandin")
print(p1)
print(nome)
