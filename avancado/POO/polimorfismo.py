from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def anda(self, msg): pass


class B(A):
    def anda(self, msg):
        print(f"B está andando {msg}")


class C(A):
    def anda(self, msg):
        print(f"C está andando {msg}")


b = B()
c = C()

b.anda("esta andando")
c.anda("parou de caminhar")

class TemERROR(Exception):
    pass

def testar():
    raise TemERROR("ERRADO!")
try:
    testar()
except TemERROR as error:
    print(f"Erro: {error}")