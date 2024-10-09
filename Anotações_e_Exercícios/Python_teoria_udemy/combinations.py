from itertools import combinations, permutations, product

def print_iter(iterador):
    print(*list(iterador), sep='\n') #tem q descompactar a lista e não o iterador
    #pois senão cada termo do iterador será contado como argumeto -> error no prompt de comando
    print()#essa função faz exatamente isso: print(*list(combinations(dados,2)))



dados = [1,2,3,4,5,6]


camisas = [['branca', 'preta', 'cinza'], ['p', 'm', 'g']]

print()
print_iter(combinations(dados,2))
print()
print_iter(permutations(dados,4))
print()
print_iter(product(*camisas))

