from dados import produtos, pessoas, lista
import functools as ft
#nova_lista = map(lambda x: x*2, lista)
new_list = [x*2 for x in lista] #faz a mesma coisa que em cima com comprehension
print(lista)
print(list(new_list))

def aumentaPreco(p):
    p["preco"] = round(p["preco"] * 1.05, 2)
    return p

'''precos = map(lambda p: p["preco"], produtos)
for preco in precos:
    print(preco) 
    AQUI EM VEZ DE USAR O LAMBDA ESTOU USANDO UMA FUNÇÃO, ABAIXO FAÇO O CONTRÁRIO'''

novo_preco = map (aumentaPreco, produtos)
for produto in novo_preco:
    print(produto)

'''def aumentaIdade(p):
    p["novaIdade"] = round(p["idade"] *1.2)
    return p
name = map(aumentaIdade, pessoas)
for pessoa in name:
    print(pessoa)
nomes = map(lambda p: p["nome"], pessoas)
for pessoa in nomes:
    print(pessoa)'''
print(45*"-")

novaLista = filter(lambda x: x > 5, lista)
print(list(novaLista))
#mesma coisa em list comprehension:
newlist = [x for x in lista if x > 5]
print(list(newlist))
print(45*"-")
'''def filtra(produto):
    if produto ["preco"] > 60:
        return True
exemplo = filter (filtra, produtos)
for produto in exemplo:
    print(produto)
    
    PODE-SE USAR O FILTER DENTRO DE UMA FUNÇÃO CASO PRECISE UTILIZÁ-LO EM MAIS DE UM LUGAR
    ASSIM SUA VARIAVEL FICA MENOR E NAO PRECISA USAR LAMBDA, PODE SIMPLIFICAR SUA VIDA!!'''

carinho = filter(lambda p: p["preco"] > 60, produtos)
for produto in carinho:
    print(produto)
print(45*"-")
def deMaior(pessoa):
    if pessoa["idade"] >= 18:
        return True
maioridade = filter(deMaior, pessoas)
for pessoa in maioridade:
    print(pessoa)
print(45*"-")

'''acumula = 0
for item in lista:
    acumula+=item
print(acumula)
-------------------------------------
redundância, vamos resolver de forma mais fácil:) '''

somaLista = ft.reduce(lambda ac, i:i + ac, lista, 0)
print(somaLista)
somaPreco = ft.reduce(lambda ac, p: round(p["preco"])+ ac, produtos, 0)
print(somaPreco)
print(f"média de preco: ", round(somaPreco/ len(produtos),2))
print(45*"-")
somaidade = ft.reduce(lambda ac, p: ac +p["idade"], pessoas, 0)
print(f"média de idade: " , somaidade/ len(pessoas))