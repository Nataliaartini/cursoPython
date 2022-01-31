import dados
import json

"""DUMPS / Dump
######################
Python          JSON
dict	        object
list, tuple	    array
str	            string
int, float  	number
True        	true
FALSE	        False
None	        null

LOADS / Load
######################
JSON	        Python
object	        dict
array	        list
string	        str
number (int)	int
number (real)	float
true	        True
false	        False
null	        None """


#Converte um dicionário em JSON
#útil para salvar informações de qualquer tipo
dados1 = json.dumps(dados.clientes_dicionario, indent=4)

#Converte JSON em um dicionário
# útil para carregar informações de qualquer tipo
dados1 = json.loads(dados.clientes_json)
print(dados1)

# Exporta dicionário para arquivo JSON
with open('clientes.json', 'w') as f:
    json.dump(clientes_dicionario, f, indent=4)

# Importa string de um arquivo JSON e converte em dicionário
with open('clientes.json', 'r') as f:
    data = json.load(f)

print(data)