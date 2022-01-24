def func():
    return "oi pessoal"

def func1(funcao):
    return funcao()
executa = func1(func)
print(executa)
print(28*"-")
def um(nome):
    return f"oi {nome}"

def dois(nome, saudacao):
    return f"{saudacao} {nome}"

def main(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

letsgo = main(um, "Natalia")
letsgo1= main(dois, "Natalia", saudacao = "Bom dia")
print(letsgo)
print(letsgo1)
