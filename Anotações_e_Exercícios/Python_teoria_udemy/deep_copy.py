from dados import produtos
import copy

novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)} for p in copy.deepcopy(produtos)
    

]


produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome']
)

produtos_ordenados_por_nome_reverso = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome'],
    reverse=True

)

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['preco']
)
#tem q usar o key= lambda para ir em cada termo da lista, se colocar so aumento_produtos da error
#nao pode tratar lista como um diconario, o key nao vai saber todos os names de produtos, so o primeiro
#por isso o key= lambda é o apropriado
print(*produtos, sep = '\n')
print()
print(*produtos_ordenados_por_preco, sep = '\n')

 