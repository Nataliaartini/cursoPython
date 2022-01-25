import itertools
indice = itertools.count()
cidades = ["Realeza", "Chapecó", "Cuiabá", "Natal", "Florianópolis"]
estados = ["PR", "SC", "MT", "RN"]
cidade_estado = zip(indice, cidades, estados) #tem que estar na ordem certa nesse caso
#print(list(cidade_estado)) #o zip só une até o tamanho da menor lista
# for i in cidade_estado:
#     print(i)
cidades_estados = itertools.zip_longest(cidades, estados, fillvalue="estado")# executa os valores da maior lista com o outro valor como none
print(list(cidades_estados)) #com fillvalue preenche com o valor que tu escolher
for indice, cidades, estados in cidade_estado: #usa o zip para ter segurança de nao gerar loop infinito
    print(indice, cidades, estados)
