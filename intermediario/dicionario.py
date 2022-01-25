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
print("string" in d3)
print("valor" in d3.values())
print(len(d3))

'''for k in d3:
    print(k)--assim acessa só os nomes das chaves, o de baixo pega o nome e o valor'''
for k, v in d3.items():
    print(k, v)
clientes = {
    "cliente1": {
        "nome": "Natalia",
        "sobrenome": "Ferrandin",
    },
    "cliente2":{
        "nome":"Natan",
        "sobrenome":"Artini",
    },
}
for clients_k, clients_v in clientes.items():
    print(f"mostra {clients_k}")
    for dados_k, dados_v in clients_v.items():
        print(f"\t{dados_k} = {dados_v}")

lista = [
    ["c1", 1],
    ["c2", 2],
    ["c3", 3],
]
d4 = dict(lista) #consigo converter listas e tuplas em dict
d4.pop("c3")
print(d4)
d4.update(d2)
print(d4)
print(28*"-")

perguntas = {
    "pergunta 1": {
        "pergunta": "quanto é 2²?",
        "respostas": {
            "a-": "2",
            "b-": "4",
            "c-": "6",
        },
        "resposta_certa": "b",
    },
    "pergunta 2":
        {
            "pergunta": "resolva a conta: 9+3*4",
            "respostas": {
                "a-": "23",
                "b-": "48",
                "c-": "21",
            },
            "resposta_certa": "c",
        },
}
acertos = 0
for chavep, chaver in perguntas.items(): #iterando sobre o dicionario com as perguntas
    print(f"{chavep}: {chaver['pergunta']}")
    for respkey, respvalue in chaver["respostas"].items(): #iterando sobre o dicionario com as respostas
        print(f"[{respkey}]: {respvalue}")
    responda = input("resposta: ")
    if responda == chaver["resposta_certa"]:
        print("Parabéns!")
        acertos+=1
    else:
        print("ops não foi dessa vez")
pergunta = len(perguntas)
porcentagem = acertos / pergunta * 100
print(f"você acertou {acertos} respostas")
print(f"isso é {porcentagem}%")
