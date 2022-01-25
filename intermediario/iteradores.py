import sys
import time

'''l1 = [1,2,3,4,5]
l1 = iter(l1)
print(next(l1))'''

def gera():
    r = []
    for n in range(10):
        yield n
        #time.sleep(0.1) #vai demorar 1 segundo para mostrar resultado na tela

g = gera ()
for v in g:
    print(v)

def gerar():
    var = "valor 1"
    yield var
    var = "valor 2"
    yield var
    var = "valor 3"
    yield var
    var = "valor 4"
    yield var
f = gerar()
for i in f:
    print(i)
l1 = [x for x in range(1000)]
l2 = (x for x in range (1000))
print(type(l1))
print(type(l2))
print(sys.getsizeof(l1))
print(sys.getsizeof(l2))
print(40*"*")
nome = "Lua"
iterador = iter(nome)
gerador = (letra for letra in nome)
for letra in gerador:
    print(letra)
print("-"* 5)
try: #se acaso eu der mais nexts do que as iteracoes que eu tenho, nao vai dar erro de stopiteration
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador)) #é exatamente o que o for faz
except:
    pass
