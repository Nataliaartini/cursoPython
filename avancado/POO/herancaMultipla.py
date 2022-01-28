class Eletronico:
    def __init__(self, nome):
        self.nome = nome
        self._ligado = False

    def ligar(self):
        if self._ligado:
            return
        self._ligado = True

    def desligar(self):
        if not self._ligado:
            return
        self._ligado = False

class Celular(Eletronico):
    def __init__(self, nome):
        super().__init__(nome)
        self.conectado = False

    def conectar(self):


