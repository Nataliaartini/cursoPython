from zipfile import ZipFile
import os

caminho = "/home/ballke-dev/Downloads/"
with ZipFile("arquivo.zip", "w") as zip:
    for arquivo in os.listdir(caminho):
        caminho_completo = os.path.join(caminho, arquivo)
        zip.write(caminho_completo)

with ZipFile("arquivo.zip", "r") as zip:
    for arquivo in zip.namelist():
        print(arquivo)

with ZipFile("arquivo.zip", "r") as zip:
    zip.extractall("descompactado")
