import os

path_finder = r"/home"
file_finder = ""

for root, directs, files in os.walk(path_finder):
    for file in files:
        if file_finder in file:
            caminho_completo = os.path.join(root, file)
            nome_arquivo, ext_arquivo = os.path.splitext(file)
            tamanho = os.path.getsize(caminho_completo)
            print(file)
