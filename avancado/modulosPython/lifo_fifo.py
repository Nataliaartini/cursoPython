from collections import deque  # para trabalhar filas

livros = list()
livros.append("HP 1")
livros.append("HP 2")
livros.append("HP 3")
livros.append("HP 4")
livros.append("HP 5")
livros.append("HP 6")
livros.append("HP 7")
livros.append("crepusculo")
livro_removido = livros.pop()  # last in, first out
print(livros)
print(livro_removido)

fila = deque(maxlen=7)  # se adicionar mais que 7 vai removendo os primeiros para adicionar o novo ao fim
fila.append("ariane")
fila.append("teobaldo")
fila.append("rafaeli")
fila.append("cacau")
fila.append("jordana")
fila.append("natanael")
fila.append("jiraya")
print(f"SAIU: {fila.popleft()}")  # para retirar o primeiro adicionado FIFO

for nome in fila:
    print(nome)

print(45*"-")

fila1 = deque()
fila1.extend([1, 2, 3, 4])
fila1.append(5)
fila1.append(6)
fila1.insert(3, 8)  # indice e conteudo

for a, i in enumerate(fila1):
    print(f"indice: {a} | elemento: {i}")

fila1.remove(4)
print(45*"=")
for a, i in enumerate(fila1):
    print(f"indice: {a} | elemento: {i}")
