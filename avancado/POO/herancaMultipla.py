class Eletronico:
    def __init__(self, nome):
        self.nome = nome
        self._ligado = False

    def ligar(self):
        if self._ligado:
            return
        self._ligado = True
        print(f"{self.nome} foi ligado com Sucesso")

    def desligar(self):
        if not self._ligado:
            return
        self._ligado = False


class LogMixin:
    @staticmethod
    def write(msg):
        with open("log.log", "a+") as f:
            f.write(msg)
            f.write("\n")

    def log_info(self, msg):
        self.write(f"INFO: {msg}")

    def log_error(self, msg):
        self.write(f"ERROR: {msg}")


class Celular(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            error = f"{self.nome} está desligado"
            print(error)
            self.log_error(error)
            return
        if self._conectado:
            error = f"{self.nome} já está conectado"
            print(error)
            self.log_error(error)
            return
        info = f"{self.nome} foi conectado com Sucesso"
        print(info)
        self.log_info(info)
        self._conectado = True

    def desconectar(self):
        if not self._conectado:
            error = f"{self.nome} está desconectado"
            print(error)
            self.log_error(error)
            return
        info = f"{self.nome} foi desconectado com Sucesso"
        print(info)
        self.log_info(info)
        self._conectado = False


celular = Celular("Motorola V3")
celular.conectar()
celular.desligar()
celular.ligar()
celular.conectar()
celular.conectar()
celular.desligar()
celular.desconectar()
celular.desligar()
celular.conectar()
celular.conectar()
