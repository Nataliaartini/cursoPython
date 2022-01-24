'''def saudacao (msg, nome):
    nome = nome.replace("a", "é")
    return f'{msg} {nome}'

var = saudacao("Boa tarde", "Natalia")
print (var)'''

def divisao(n1, n2):
    if n1 == 0 or n2 == 0:
        return
    return n1/n2

divide = divisao(8,5)
if divide:
    print(divide)
else:
    print("não existe divisão por 0, tente outro numero")

def dumb ():
    return 1

print(dumb(), type(dumb()))

def example():
    return ("1", "2")
var = example()
print(var, type(var))
