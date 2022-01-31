from abstracao import Conta


# esse arquivo foi criado para fazer classe e funcao para sacar conforme metodo abstrato definido no arquivo abstracao


class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade


class Cliente(Pessoa):
    def __init__(self, nome, idade, conta):
        super().__init__(nome, idade)
        self.conta = None

    def insere_conta(self, conta):
        self.conta = conta


class Banco:
    def __init__(self):
        self.agencias = [1111, 2222, 3333]
        self.cliente = []
        self.contas = []

    def insere_cliente(self, cliente):
        self.cliente.append(cliente)

    def insere_conta(self, conta):
        self.contas.append(conta)

    def autentica(self, cliente):
        if cliente not in self.cliente:
            return False
        if cliente.conta not in self.contas:
            return False
        if cliente.conta.agencia not in self.agencias:
            return False

        return True


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print("Saldo insuficiente")
            return
        self.saldo -= valor
        self.detalhes()


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=1000):
        super().__init__(agencia, conta, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def sacar(self, valor):
        if (self.saldo + self._limite) < valor:
            print("Saldo insuficiente")
            return
        self.saldo -= valor
        self.detalhes()


banco = Banco()
cliente1 = Cliente("Natalia", 21, 254166)
cp = ContaPoupanca(1111, 254166, 0)  # agencia, conta e saldo
cliente1.insere_conta(cp)
cliente2 = Cliente("Tainara", 24, 451826)
cc = ContaCorrente(1111, 451826, 0, 500)  # agencia, conta, saldo e limite
cliente2.insere_conta(cc)

banco.insere_cliente(cliente1)
banco.insere_conta(cp)

if banco.autentica(cliente1):
    cliente1.conta.depositar(65)
    cp.depositar(65)
    cp.sacar(6.9)
    cp.depositar(15)
    cp.sacar(30)
    cp.sacar(80)
    cp.sacar(1)
    cp.depositar(5000)
else:
    print("Cliente não autorizado")

banco.insere_cliente(cliente2)
banco.insere_conta(cc)

print(45 * "*")
if banco.autentica(cliente2):
    cc.depositar(1500)
    cc.sacar(10000)
    cc.sacar(1700)
    cc.sacar(50)
    cc.depositar(5000)
else:
    print("Cliente não autorizado")
print(45 * "*")
print(cliente1.nome, cliente1.conta)
print(cliente2.nome, cliente2.conta)
