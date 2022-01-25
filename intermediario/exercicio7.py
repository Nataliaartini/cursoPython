lista1 = [1,2,3,4,5]
lista2 = [1,2,3]
# lista3 = zip(lista1, lista2)
# lista3 = list(lista3)
# for i in lista3: ##outra forma de resolver, código menos eficiente
#     a = i[0]+i[1]
#     print(a)
'''usando comprehension list'''
soma = [x+y for x,y in zip(lista1, lista2)]
print(soma)