from time import sleep

perguntas = [{'pergunta': 'Quanto é 2 + 2?',
             'Ópções': [1, 2, 3, 4],
             'indice_resposta': 3},
             
             {'pergunta': 'Quanto é 10/2?',
             'Ópções': [5, 23, 3, 34],
             'indice_resposta': 0},
             
             {'pergunta': 'Quanto é 22 x 11?',
             'Ópções': [121, 242, 233, 324],
             'indice_resposta': 1},
             ]

acertos = 0
erros = 0

for pergunta in perguntas:
    print('Pergunta:', pergunta['pergunta'])
    print()

    for i, opcao in enumerate(pergunta['Ópções']):
        print(f'{i}) {opcao}')
    print()

    try:
        escolha = int(input('Resposta:'))
        if escolha == pergunta['indice_resposta']:
            print('Acertou')
            acertos += 1
        else:
            print('ERROU')
            erros += 1
    except ValueError:
        print('ERROU! SÓ O NÚMERO DAS ALTERNATIVAS')
        erros += 1
        continue

    print()
    sleep(1)

print(f'Acertos: {acertos}')
print(f'Erros: {erros}')
    