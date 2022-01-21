x = 0
y = 0
while x<5:
    while y < 5:
        y+=1
        x+=1
        print(f"x= {x} y= {y}")
        print(28 * "-")
while True:
    a= int(input("digite um numero: "))
    b= int(input("digite um numero: "))
    o= input("digite a operação: ")

    if o == "-":
        print(a-b)
    elif o == "+":
        print(a+b)
    else:
        print("operação inválida")
    e = input("deseja sair? s | n: ")
    if e == "s":
        break
print(28 * "-")

#aula 15
frase = "o rato roeu"
TAM= len(frase)
contador = 0
frase1 = ""
while contador < TAM:
    letra = frase[contador]
    if letra == "r":
        frase1+= "R"
    else:
        frase1 += letra
    print(f"{frase1}")
    contador +=1
print(28 * "-")

#aula 16
for i in range (6,20,4):
    print(i)
print(28 * "-")
for n in range (20,10,-2):
    print(n)
print(28 * "-")
l1=[1,2,3]
l2=[9,8,7]
l1.extend(l2)
print(l1)
# print(max(l1))
# print(min(l1))
l2.append("lista")
print(l2)
print(28 * "-")
soma = 0
for valor in l1:
    soma = soma + valor
print(f"a soma de l1 é: {soma}")
print(28 * "-")
for i in l2:
    print(f"os tipos de l2 são: {type(i)}")
print(28 * "-")

# joguinho
secreta = "sherlock holmes"
digitadas = []
while True:
    letra = input("digite uma letra: ")
    if len(letra) > 1:
        print("digite apenas 1 letra.")
        continue
    digitadas.append(letra)
    if letra in secreta:
        print("essa letra existe na palavra secreta")
    else:
        print("essa letra não existe na palavra secreta")
        digitadas.pop()
    aux = ''
    for i in secreta:
        if i in digitadas:
            aux += i
        else:
            aux += "*"
    print(aux)

    if len(digitadas) >= 5:
        print("e aí, já sabe qual a palavra secreta?")
        break
