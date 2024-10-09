cidades = ['Rio de janeiro', 'São Paulo','João Pesoa']
uf = ['RJ', 'SP', 'PB', 'RS']

def zipper(l1, l2):
    indice_limite = min(len(l1), len(l2))

    return[(l1[i], l2[i]) for i in range(indice_limite)] 
#o (l1[i], l2[i]) significa que quer uma cidade e uma uf numa tupla dentro da lista


print(zipper(cidades, uf)) #primeira froma: função do usuário

print(list(zip(cidades, uf)))# segunda forma: função do python -> o list é necessário pois zip é um iterator

from itertools import zip_longest
print(list(zip_longest(cidades, uf, fillvalue= 'CIDADE NÃO DECLARADA'))) #fillvalue é tipo um raise do none
# terceira forma: com um módulo só que se baseia na maior lista 
