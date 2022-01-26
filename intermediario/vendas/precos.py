import formata.preco
def aumento(valor, porcentagem):
    r = valor + (valor * (porcentagem/100))
    r = formata.preco.real(r)
    return r

