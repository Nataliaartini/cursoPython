x = 0
y = 0
while x<5:
    while y < 5:
        y+=1
        x+=1
        print(f"x= {x} y= {y}")
        print(28 * "-")
'''while True:
    a= int(input("digite um numero: "))
    b= int(input("digite um numero: "))
    o= input("digite a operação: ")
    e= input("deseja sair? S | N: ")

    if o == "-":
        print(a-b)
    elif o == "+":
        print(a+b)
    else:
        print("operação inválida")
    if e == "S":
        break'''
print(28 * "-")

#aula 15
frase = "o rato roeu a roupa do rei de roma"
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
for i in range (6,50,4):
    print(i)
print(28 * "-")
for n in range (20,10,-1):
    print(n)
print(28 * "-")

