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