import funcoes_CNPJ

cnpj = funcoes_CNPJ.valida("12.321.593/0001-77")
cnpj1 = funcoes_CNPJ.valida("04.252.011/0001-10")
cnpj2 = funcoes_CNPJ.valida("00.000.000/0000-00")
cnpj3 = funcoes_CNPJ.valida("123")
cnpj4 = funcoes_CNPJ.valida("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
print(50*"*")
for i in range (5):
    new_cnpj = funcoes_CNPJ.gera()
    funcoes_CNPJ.valida(new_cnpj)