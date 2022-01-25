import types
import itertools as it
var = ((x, y) for x, y in zip("oi", "oi"))
print(isinstance(var, types.GeneratorType))
contador = it.count(start=3, step=3)
for i in contador:
    print(i)
    if i >= 15:
        break
print(25*"-")
exemplo = it.count(start=0.5, step=0.05)
for j in exemplo:
    print(round(j, 2))
    if j >= 1:
        break
print(45*"-")
alunos = ["ana", "luiz", "cleiton", "pedro", "bruna", "carol", "joana", "bia", "joao", "maria"]
for grupo in it.combinations(alunos, 2):
    print(grupo)
print(45*"-")
for grupos in it.permutations(alunos,2):
    print(grupos)
print(45*"-")
estudante = [
    {"nome":"ana", "nota": 7.3},
    {"nome":"luiz", "nota": 6.9},
    {"nome":"cleiton", "nota": 9.1},
    {"nome":"pedro", "nota": 8.5},
    {"nome":"clau", "nota": 8.5},
    {"nome":"everton", "nota": 8.5},
]
ordena = lambda item: item["nota"]
estudante.sort(key=ordena) #tem que estar ordenado para usar o groupby e funcionar
agrupados = it.groupby(estudante, ordena)
for group, valores in agrupados:
    print(f"grupo: {group}")
    qtd = len(list(valores))
    print(f"{qtd} alunos tiraram a nota {group}")
