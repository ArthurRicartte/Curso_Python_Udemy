produtos = [
    {'nome': 'produto 5', 'preco':  10.00},
    {'nome': 'produto 1', 'preco':  22.32},
    {'nome': 'produto 3', 'preco':  10.11},
    {'nome': 'produto 2', 'preco':  105.87},
    {'nome': 'produto 4', 'preco':  69.90}
]
def print_iter(iterador):
    print(*list(iterador), sep='\n')


def filtar_precos(preco):
    return preco['preco'] > 10
filtrados = filter(filtar_precos, produtos) 

#filtrados = filter(lambda p: p['preco'] > 10, produtos) --> outra forma de fazer


print_iter(filtrados)

