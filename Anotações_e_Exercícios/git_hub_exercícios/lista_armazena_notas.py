lista_notas = []

def media(*args):
    return sum(args)/4



for nota in range(4):
    n = float(input(f'Digite a nota {nota + 1}:'))
    lista_notas.append(n)

maior_nota = max(lista_notas)
menor_nota = min(lista_notas)

print('-*-'*10)
for nota_da_lista in lista_notas:
    print(f'{nota_da_lista:.1f}')
print('-*-'*10)

media_notas = media(*lista_notas)

print(f'Média final:{media_notas:.1f}')
print(f'Maior nota: {maior_nota:.1f}')
print(f'Menor nota: {menor_nota:.1f}')
print('-*-'*10)

if media_notas >= 7:
    print('PARABENS VOCÊ PASSOU.')
else:
    print('VAI FAZER RECUPERAÇÃO!')
    nota_final = float(input('Digite a nota final do aluno:'))
    lista_notas.append(nota_final)
    media_final = media(*lista_notas)

    print('-*-' *20)
    for notas_finais in lista_notas:
        print(f'{notas_finais:.1f}')
    print('-*-' *20)
    
    print(f'Média final: {media_final:.1f}')
    print(f'Maior nota: {max(lista_notas)}')
    print(f'Menor nota: {min(lista_notas)}')
    
    if media_final < 5:
        print('Situação: reprovado')
        
    else:
        print('Situação: aprovado')
    print('-*-' *20)


print('CABOU')
