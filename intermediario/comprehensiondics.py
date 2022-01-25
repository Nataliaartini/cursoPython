lista = [
    ("k1", 13),
    ("k2", 12),
]
d1 = {x.upper(): y*2 for x, y in lista}
print(d1)
d2 = {x: y for x, y in enumerate(range(5))}
print(d2)

d3 = {f"chave:{x}":x for x in range(5)}
print(d3)