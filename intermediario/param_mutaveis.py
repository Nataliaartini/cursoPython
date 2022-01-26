def list_clients(client_iteravel, lista=[]):
    lista.extend(client_iteravel)
    return lista


clientes_antigos = list_clients(["josé", "joão", "maria", "pedro", "umberto"])
clientes_novos = list_clients(["lucas", "ricardo", "everton"])

print(clientes_antigos)
print(clientes_novos)
