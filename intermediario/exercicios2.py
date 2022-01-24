def saudacao (msg, nome):
    return f'{msg} {nome}'
var = saudacao("Boa tarde", "Natalia")
print (var)

def soma(a,b,c):
    return (a+b+c)
somar = soma(1,2,3)
print(somar)

def percent(d,e):
    f = ((d*e)/100)+d
    return f
preco= percent(100, 5)
print(preco)

def fizzbuzz(g):
    if g%3 == 0 and g%5 == 0:
        return f"fizzbuzz, {g}"
    if g%5 == 0:
        return f"buzz, {g}"
    if g%3 == 0:
        return f"fizz, {g}"
    return g
teste = fizzbuzz(15)
print(teste)

from random import randint
for i in range(2):
    aleatorio = randint(0, 100)
    print(fizzbuzz(aleatorio))
