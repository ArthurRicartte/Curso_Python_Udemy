dados = []
ponderar = lambda n1,n2: (n1*4 + n2*6)/10
def analisa_notas(media):
    if media < 5:
        print('colocação: D')
        return 'D'
    elif media < 7:
        print('colocação: C')
        return 'C'
    elif media < 9:
        print('colocacao: B')
        return 'B'
    else:
        print('colocação: A')
        return 'A'

for c in range(10):
    sistema_notas_alunos = []
    
    aluno_digitado = input(f'digite o nome do aluno {c+1}:')
    a1 = float(input(f'Primeira nota de {aluno_digitado}:'))
    a2 = float(input(f'Segunda nota de {aluno_digitado}:'))
    media_final = round(ponderar(a1,a2),1)
    
    sistema_notas_alunos.append(aluno_digitado)
    sistema_notas_alunos.append(a1)
    sistema_notas_alunos.append(a2)
    sistema_notas_alunos.append(analisa_notas(media_final))
    dados.append(sistema_notas_alunos)
    print()
    print('-*-' * 20)
    
    for aluno in sistema_notas_alunos:
        print(aluno)

   
    
    print(f'Média final: {media_final}')
    analisa_notas(media_final)
    print('-*-' * 20)
    print()

print(*dados, sep='\n')



     