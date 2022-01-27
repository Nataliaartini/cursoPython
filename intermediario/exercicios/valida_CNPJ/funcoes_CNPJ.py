import re
import random as rd

REGRESSIVOS = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def valida(cnpj):
    cnpj = rm_pontuacao(cnpj)
    print("\n", cnpj)
    try:
        if not_sequencia(cnpj):
            print("CNPJ inválido, não pode ser sequencial")
            return cnpj
    except:
        print("CNPJ INVÁLIDO")
        return False
    try:
        aux_cnpj = calcula(cnpj, 1)
        aux_cnpj = calcula(aux_cnpj, 2)
    except Exception as e:
        print("CNPJ INVÁLIDO")
        return False
    if aux_cnpj == cnpj:
        print("CNPJ validado")
    else:
        print("CNPJ inválido")


def calcula(cnpj, digito):
    if digito == 1:
        regressivos = REGRESSIVOS[1:]
        aux_cnpj = cnpj[:-2]
    elif digito == 2:
        regressivos = REGRESSIVOS
        aux_cnpj = cnpj
    else:
        return None
    total = 0
    for indice, regressivo in enumerate(regressivos):
        total += int(cnpj[indice]) * regressivo
    digito = 11 - (total % 11)
    digito = digito if digito <= 9 else 0
    return f"{aux_cnpj}{digito}"


def not_sequencia(cnpj):
    sequencia = cnpj[0] * len(cnpj)
    if sequencia == cnpj:
        return True
    else:
        return False


def rm_pontuacao(cnpj):
    return re.sub(r"[^0-9]", "", cnpj)

def gera():
    primeiro_digito = rd.randint(0,9)
    segundo_digito = rd.randint(0,9)
    sc_bloco = rd.randint(100,999)
    td_bloco = rd.randint(100,999)
    qrt_bloco = "0001"
    inicio_cnpj = f"{primeiro_digito}{segundo_digito}{sc_bloco}{td_bloco}{qrt_bloco}00"
    new_cnpj = calcula(inicio_cnpj, 1)
    new_cnpj = calcula(new_cnpj, 2)

    return new_cnpj
