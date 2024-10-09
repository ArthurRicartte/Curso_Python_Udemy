def adicona_clientes(nome, lista = None):
    if lista is None:
        lista = []
    
    lista.append(nome)

    return lista

#posso criar uma lista fora pra cada cliente tmb
cliente1 = adicona_clientes('ZORO')
adicona_clientes('Luffy', cliente1)
print(cliente1)


cliente2 = adicona_clientes('Nami')
adicona_clientes('Robbin', cliente2) 
print(cliente2) 
