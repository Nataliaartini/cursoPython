a= 1
print(f"{a:0>10}") #preenche com 0 à esquerda
print(f"{a:0<10}") #preenche com 0 à direita
print(f"{a:0^10}") #deixa o numero no meio de 0
print(f"{a:0>10.2f}")
nome = "Natalia"
sobrenome= "Ferrandin"
nomeCompleto= '{1}, {0}'.format(nome, sobrenome)
print(nomeCompleto)
print(nomeCompleto.lower())
print(nomeCompleto.upper())
print(nomeCompleto.title()) #primeiras letras maiusculas
print(28 * "-")

texto = "Olá pessoal!"
print(texto[:-1]) #exclui o ultimo
print(texto[-1])
print(texto[:7])
print(texto[3:9])
