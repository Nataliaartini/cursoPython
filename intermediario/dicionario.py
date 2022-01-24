#dicionario suporta um par de chave e um valor
d1 = dict(chave1 = "valor da chave", chave2 = "chave 2")
d1["nova_chave"] = "chave nova"
print(d1["nova_chave"])
print(d1)
d2 = {"chave": "esse é outro jeito de declarar chaves"}
print(d2)
d3 = {
    "string" : "valor",
    123: "outro valor",
    (1,2,3,4) : "tupla",
}
print(d3 [(1,2,3,4)])
print(d1.get("chave3"))
