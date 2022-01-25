from dados import produtos, pessoas, lista
#nova_lista = map(lambda x: x*2, lista)
new_list = [x*2 for x in lista] #faz a mesma coisa que em cima com comprehension
print(lista)
print(list(new_list))
precos = map(lambda p: p["preco"], produtos)
for preco in precos:
    print(preco)
