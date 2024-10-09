from functools import partial

produtos = [
    {'nome': 'produto 5', 'preco':  10.00},
    {'nome': 'produto 1', 'preco':  22.32},
    {'nome': 'produto 3', 'preco':  10.11},
    {'nome': 'produto 2', 'preco':  105.87},
    {'nome': 'produto 4', 'preco':  69.90}
]

def print_iter(iterador):
    print(*list(iterador), sep = '\n')#coloca tudo dentro de uma lista(o list faz isso) e depois desempacota*
    print()#restando só os dicionários
    #se desempacotar assim: *iterador cada dicionário será contado como um argumento
    #pode fazer só *iterador, sep = '\n' que funciona da mesma forma
def aumenta_porcentagem(valor, porcentagem): 
    return round(valor * porcentagem, 2)
# bom deixar valor, porcentagem nessa ordem pra não confundir no partial e nem gerar erros

aumenta_dez_porcento = partial(aumenta_porcentagem,porcentagem= 1.1)#partial serve como uma clousure function
#tecnicamente como uma função de primeira classe
def muda_precos(valor):
    return {**valor, 'preco': aumenta_dez_porcento(valor['preco'])}

novos_produtos = list(map(muda_precos,produtos))# o map mapeia os valores q vai utilizar e cria uma list
#comprehention p primeiro termo é a função q vai usar como base e o segundo o que vai alimentar os parâmetros
#da função

print_iter(produtos)
print_iter(novos_produtos)
