from itertools import groupby


alunos = [
    {'nome': 'luffy', 'nota': 'D'},
    {'nome': 'zoro', 'nota': 'D'},
    {'nome': 'Namir', 'nota': 'B'},
    {'nome': 'ussop', 'nota': 'C'},
    {'nome': 'sanji', 'nota': 'A'}
]

def orientador(chave):
    return chave['nota']

alunos_organuzados = sorted(alunos, key = orientador)#não precisa dos () pois não vamos passar argumentos 
grupos = groupby(alunos_organuzados, key = orientador)


for chave, grupo in grupos: #grupo é um iterável e não dá pra printar ele 
    print(chave)
    for aluno in grupo:#por isso o segundo for é importante pra exibir os alunos
        print(aluno)
