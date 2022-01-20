
f= input("digite o numero que deseja verificar: ")
if f.isdigit():
    f = int(f)
    if f%2 == 0:
        print(f"{f} é um número par")
    else:
        print(f"{f} é um número ímpar")
else:
    print("digite um numero inteiro para fazer a verificação")
print(28 * "-")

hora= input("que horas são aí onde tu tá? ")
if hora.isdigit():
    hora = int(hora)
    if hora >= 0 and hora <= 11:
        print("Bom dia lindo usuário")
    elif hora >= 12 and hora <= 17:
        print("Boa tarde lindo usuário")
    elif hora >=18 and hora <= 23:
        print("Boa noite lindo usuário")
    else:
        print("Horário inválido")
else:
    print("Horário inválido")
print(28 * "-")

nome = input("Olá, qual o seu nome? ")
if len(nome)<=4:
    print(f"{nome} você tem um lindo nome curto")
elif len(nome)>4 and len(nome)<=6:
    print(f"{nome} você tem um lindo nome normal")
else:
    print(f"{nome} você tem um lindo nome grande")
print(28 * "-")
