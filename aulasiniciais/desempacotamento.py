clientes = ["maria", "pedro", "guilherme", "alexandre"]
c1, c2, *new_lista = clientes
print(c1, new_lista)
# *_ significa que a variavel nao sera usada

a = 15
b = "luz"
c= "newton"
a, b, c = c, a, b
print(f"a= {a}, b= {b} e c= {c}")
print(28*"-")

# aula 20
logged_user = True
msg = "Usuário logado" if logged_user else "Usuário precisa fazer login"
print(msg)
print(28*"-")

nome = input("qual o seu nome? ")
'''if nome:
    print(nome)
else:
    print("campo 'nome' vazio")'''
print(nome or None or False or "campo 'nome' vazio") #if ternario

