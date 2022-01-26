try:
    a = 1/0
except NameError as erro:
    print("Erro do desenvolvedor, fale com ele: ", erro)
except (IndexError, KeyError) as erro:
    print("Erro de indice ou chave.")
except Exception as erro:
    print("Ocorreu um erro inesperado.")
else:
    pass
finally:
    a = ''
print(a)
print(45*"-")

'''def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError as error:
        print("Não existe divisão por 0, tente outro valor")
        raise #faz o log da exceção e relança ela para o try de baixo
try:
    print(divide(2,0))
except:
    print("erro")       #só é executado por causa do raise de cima
    OUTRA FORMA DE FAZER ISSO SEM USAR O TRY: '''
def divide(n1,n2):
    if n2 == 0:
        raise ValueError("Não pode dividir por 0")
    return n1/n2
try:
    print(divide(2,0))
except ValueError as error:
    print(error)