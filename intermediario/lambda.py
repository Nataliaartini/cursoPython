def funcao(arg, arg2):
    return arg * arg2
var = funcao(6, 5)
print(var)
#mesma funcao em formato lambda
a = lambda x, y: x*y
print(a(4,8))

lista = [
    ["p1", 13.2],
    ["p2", 5.6],
    ["p3", 9.5],
]
'''def dizlugar(item):
    return item[1] #indice 1 que é preco'''

#lista.sort(key=dizlugar) - ordena pelo menor preco
lista.sort(key=lambda item: [1], reverse=True) #aqui o lambda elimina uma função só pra retornar um indice
print(decrescente)
'''pode ser usado a funcao print sorted lista com o lambda que é o mesmo resultado mas sem alterar lista original'''

