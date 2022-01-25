#sets parecem dicionarios mas nao tem chaves e nem indices, somente valores
s1 = {1,2,3}
s2 = set() #assim se cria um set vazio
s2.add(1)
s2.add(2)
s2.discard(1)
s2.update("b")
#sets geralmente são usados para remover elementos duplicados de listas, exemplo:
l1 = [1,2,3,3,3,5,6,4,6,5,"a","a"]
l1 = set(l1) #remove duplicados
l1 = list(l1) #agora faço virar lista de novo
print(l1)
print(28*"-")
s3 = {1,2,3,4,5,6}
s4 = {4,5,6,7,8,9}
s5 = s3 | s4 #funcao union para sets
s6 = s3 & s4 #intersection pega os elementos iguais nos dois sets
s7 = s3 - s4 #pega elementos apenas no set da esquerda
s8 = s3 ^ s4 #pega os diferentes de cada set
print(s5)
print(s6)
print(s7)
print(s8)

print(40*"*")
print("EXERCICIO 4")
"""
-> É uma lista de listas de números inteiros
-> As listas internas tem o tamanho de 10 elementos
-> As listas internas contém números entre 1 a 10 e eles podem ser duplicados
Exercício
-> Crie uma função que encontra o primeiro duplicado considerando o segundo
    número como a duplicação. Retorne a duplicação considerada.
        Requisitos:
            A ordem do número duplicado é considerada a partir da segunda
            ocorrência do número, ou seja, o número duplicado em si.
            Exemplo:
                [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
                [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
            Se não encontrar duplicados na lista, retorne -1
"""
listas_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]
def encontra_primeiro_duplicado(lista):
    check = set ()
    first_duplicado = -1
    for numero in lista:
        if numero in check:
            first_duplicado = numero
            break
        check.add(numero)
    return first_duplicado

for lista1 in listas_inteiros:
    print(lista1, encontra_primeiro_duplicado(lista1))
