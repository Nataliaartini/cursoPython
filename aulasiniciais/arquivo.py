#aula 1
print('Hello guys!')
#comente seus códigos parça
"""documentação também é importante"""
print("Natalia", "Ferrandin ", sep="_")
print(28*"-")

#aula 2
print('000', '000', '000', sep='.', end='-')
print('01 ')
print(28*"-")


#aula 3
print("isso é 1 'string'.")
print(5)
print("isso é int ")
print(28*"-")

#aula 4
print('Nome: Natalia', type("Natalia"))
print("idade:", 21, type(21))
print("altura:",1.60, type(1.60))
print('é maior de idade?',21>=18 , type(21>=18),)
print(28*"-")

#aula 5
print("10 x 10 =",10*10)
print("3+8 = ", 3+8)
print("9/3 = ", 9/3)
print("3² = ", 3**2)
print("divisão inteira de 15/8 = ", 15//8)
print("resto da divisão 15/8 = ", 15%8)
print(28*"-")

#aula 6
nome = "Natalia"
idade = 21
altura = 1.60
maior = idade > 18
peso = 54
print("Nome: ",nome)
print("idade: ", idade)
print("altura: ", altura)
print("de maior?", maior)
print("peso = ", peso ,"kg")
print(f"o IMC de {nome} é: {peso/(altura*altura):.2f}")
print(28*"-")

#aula 7
nasc = 2022- idade
print(f"{nome} tem {idade}, {altura} de altura e pesa {peso} kg")
print(f"o IMC de {nome} é: {peso/(altura*altura):.2f}")
print(f"{nome} nasceu no ano de {nasc}")
print(28*"-")

#aula 8
nome=input("qual seu nome? ")
idade=int(input("qual sua idade? "))
nasc= 2022-idade
print(f"olá {nome}")
print(f"{nome} nasceu no ano de {nasc}")
print(28*"-")
