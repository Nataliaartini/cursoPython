def saudacao (msg, nome):
    nome = nome.replace("a", "é")
    return f'{msg} {nome}'

var = saudacao("Boa tarde", "Natalia")
print (var)
