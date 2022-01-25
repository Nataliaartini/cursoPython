#sets parecem dicionarios mas nao tem chaves e nem indices, somente valores
s1 = {1,2,3}
s2 = set() #assim se cria um set vazio
s2.add(1)
s2.add(2)
s2.discard(1)
s2.update("b")
#sets geralmente são usados para remover elementos duplicados de listas, exemplo:
lista = [1,2,3,3,3,5,6,4,6,5,"a","a"]
lista = set(lista) #remove duplicados
lista = list(lista) #agora faço virar lista de novo
print(lista)
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