from time import time
from time import sleep
def master(funcao):
    def puppets(*args, **kwargs):
        print("decorada")
        funcao(*args, **kwargs)
    return puppets

@master
def callmyname():
    print("MASTER!! MASTER!!")

@master
def outra(msg):
    print(msg)

"""callmyname=master(callmyname)usando o @master em cima dessa funcao nao precisa dessa linha para executar a master"""

callmyname()

outra("I''ll hear your scream")
print(45*"*")

def velocidade(func):
    def interna(*args, **kwargs):
        start_time = time()
        resultado = func(*args, **kwargs)
        end_time = time()
        tempo = (end_time - start_time) *1000
        print(f"\na função '{func.__name__}' foi executada em {tempo:.2f}ms.")
        return resultado
    return interna

@velocidade
def demora():
    for i in range(666):
        print(i, end = "")

demora()