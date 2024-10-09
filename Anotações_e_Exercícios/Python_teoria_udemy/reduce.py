from functools import reduce

produtos = [
    {'nome': 'produto 5', 'preco':  10.00},
    {'nome': 'produto 1', 'preco':  22.32},
    {'nome': 'produto 3', 'preco':  10.11},
    {'nome': 'produto 2', 'preco':  105.87},
    {'nome': 'produto 4', 'preco':  69.90}
]

def funcao_reduce(acumulador, produto):
    print('acumulador', acumulador)
    print('produto', produto)
    print()
    return acumulador + produto['preco']

total = reduce(funcao_reduce, produtos, 0)#esses argunmentos seguem a ordem do reduce
#a função, o iterável, e o inicial, mas o 0 seria o acumulador e os produtos o produto da função 
print(round(total, 2))

#total = reduce(lambda ac, p: ac + p['preco'], produtos, 0) #uma outra forma de fazer


