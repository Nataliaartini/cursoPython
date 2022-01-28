from abstracao import Conta


# esse arquivo foi criado para fazer classe e funcao para sacar conforme metodo abstrato definido no arquivo abstracao

class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print("Saldo insuficiente")
            return
        self.saldo -= valor
        self.detalhes()


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self_limite

    def sacar(self, valor):
        if (self.saldo + self._limite) < valor:
            print("Saldo insuficiente")
            return
        self.saldo -= valor
        self.detalhes()


cp = ContaPoupanca(1111, 2222, 0)
cp.depositar(65)
cp.sacar(6.9)
cp.depositar(15)
cp.sacar(30)
cp.sacar(80)
cp.sacar(1)
cp.depositar(5)
print(45 * "*")
cc = ContaCorrente(1111, 3333, 0, 500)
cc.depositar(100)
cc.sacar(250)
cc.sacar(351)
cc.depositar(700)
