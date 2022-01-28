class CarrinhoCompras:
    def __init__(self):
        self.produtos = []

    def insere_produto(self, produto):
        self.produtos.append(produto)

    def lista_produtos(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total

class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

carrinho = CarrinhoCompras()
prod1 = Produto("camisa", 50)
prod2 = Produto("short", 90)
prod3 = Produto("meias", 25)

carrinho.insere_produto(prod1)
carrinho.insere_produto(prod2)
carrinho.insere_produto(prod3)
carrinho.insere_produto(prod1)

carrinho.lista_produtos()
print(carrinho.soma_total())
