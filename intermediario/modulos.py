import sys
import random as rd
import math
import datetime
from dados import *
import meumodulo
from vendas import precos
from vendas.formata import preco
PI = math.pi
print(sys.platform)
print(rd.randint(0,13))
def dobra(lista):
    return [x*2 for x in lista]
print(dobra(lista))
def multiplica(lista):
    r = 1
    for i in lista:
        r*=i
    return r
print(multiplica(lista))
print(PI)
print(meumodulo.mensagem())
data = datetime.datetime.now()
dataformata = data.strftime("%d/%m/%Y %H:%M")
print(f"estamos em :",dataformata)
print(45*"*")

preco = 49.9
novopreco = precos.aumento(preco,15)
print(novopreco)
print(45*"*")
