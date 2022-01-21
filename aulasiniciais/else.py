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