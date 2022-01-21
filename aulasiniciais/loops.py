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
l2.append("lista")
print(l2)

