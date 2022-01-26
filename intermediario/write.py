#as duas formas a seguir não são recomendadas para se trabalhar com arquivos em python
file = open("abc.txt", "w+")
file.write("olá,\n" "meu nome é:\n" "Natalia\n")
file.seek(0, 0)#posição onde começa e posicao do fim do arquivo
print(file.read())
print(28*"-")
file.seek(0, 0) #toda modificacao tem que indicar novamente o inicio do arquivo
print(file.readline(),end = '')#end= '' faz ignorar quebras de linhas
print(28*"-")
file.seek(0, 0)
print(file.readlines())
print(28*"-")
file.seek(0 ,0)
for linha in file:
    print(linha, end = '')
print(28*"-")
file.close()

try:
    file1 = open("outro.txt", "w+")
    file1.write("documentação")
    file1.seek(0, 0)
    print(file1.read())
finally:
    file1.close()
print(28*"-")
#esse modo é mais recomendada por ser um gerenciador que fecha arquivo quando termina de se executar evitando problemas
with open("another.txt", "w+") as file2:
    file2.write("maneira correta de trabalhar files em python")
    file2.seek(0)
    print(file2.read())
print(28*"-")
with open("arquivo.txt", "a+") as file3:#cada vez que executa adiciona o que está escrito nele
    file3.write("arquivo appending\n")
    file3.seek(0)
    print(file3.read())
#para remover só importar modulo os e usar funcao remove e o arquivo

import json
d1 = {
    "pessoa1": {
        "nome": "Natalia",
        "idade": 20,
    },
    "pessoa2": {
        "nome": "natan",
        "idade": 25,
    },
}
d1_json = json.dumps(d1, indent = True)

with open("using.json", "w+") as arquivo:
    arquivo.write(d1_json)
