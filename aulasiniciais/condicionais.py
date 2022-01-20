#aula 9
if (2>9):
    print("2 é maior que 9")
else:
    print("2 é menor que 9")

a=5.6
b=5.5
expressao= (a==b)
print(expressao)

if a>b and b<6:
    print("ok")

user = int(input("login: "))
password = int(input("senha: "))
login = 1
senha = 1
if user == login and password == senha:
    print("login efetuado com sucesso")
else:
    print("usuário ou senha incorretos, tente novamente")
