lista = ["oi", "tudo", "bem?"]
init = False
for i in lista:
    if i.startswith("oi"):
        print(i)
    else:
        print("error")
for j in lista:
    if j.startswith("t"):
        init = True
if init:
    print("existe uma palavra com inicio t")
else:
    print("nenhuma dessas palavras começa com t")
print(28*"-")

# aula 18
string = "eu sou uma moça, eu tenho 20 anos"
vetor = string.split(",") #vai dividir em duas strings separadas na virgula
vetorcount = string.split(" ")
palavra = " "
contagem = 0
for n in vetorcount:
    print(f"{n} apareceu {vetorcount.count(n)}X.")
    qtd = vetorcount.count(n)
    if qtd > contagem:
        contagem = qtd
        palavra = n
print(28*"-")
print(f"{palavra} {contagem}X, foi o que mais apareceu")
print(28*"-")
string2 = ".".join(vetorcount) #junta as palavras com .
print(string2)
for i,j in enumerate(vetorcount):
    print(i,j)
print(28 * "-")

lista = [
    [1,"- cliente 1"],
    [3,"- cliente 3"],
]
for id,nome in enumerate(lista):
    print(id,nome)
    print(lista[0][1])
