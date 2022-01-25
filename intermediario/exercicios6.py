carrinho = []
carrinho.append(("produto", 23.6))
carrinho.append(("produto",85.4))
carrinho.append(("produto", 48.2))

total = sum([float(valor) for produto, valor in carrinho ])
print(total)