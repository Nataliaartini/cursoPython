'''arquivo = open("abc.txt", "w")
arquiv.write("alguma coisa")
arquivo.close()'''

#with open("ab.txt", "w") as arquivo:
#   arquivo.write("alguma coisa")

class Arq:
    def __init__(self, arquivo, modo):
        print("abre arquivo")
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        print("retorna arquivo")
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("fecha arquivo")
        self.arquivo.close()

with Arq("ab.txt", "w") as arquivo:
   arquivo.write("alguma coisa")

print(45*"*")

from contextlib import contextmanager

@contextmanager
def novoArquivo(arq, mode):
    try:
        novoArquivo = open(arq, mode)
        print("abrindo arquivo")
        yield novoArquivo
    finally:
        print("arquivo fechado")
        novoArquivo.close()

with novoArquivo("abc.txt", "w") as newArquivo:
    newArquivo.write ("primeira linha")

import encapsulamento
help(encapsulamento)
"""exemplo de como acessar documentação de um código"""
