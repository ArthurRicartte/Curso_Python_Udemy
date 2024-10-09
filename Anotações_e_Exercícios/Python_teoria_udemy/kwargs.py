pessoa = {'nome': 'Arthur', 'sobrenome': 'Ricartte'}

dados = {'altura': 1.68, 'idade': 17}


pessoa_completa = {**pessoa, **dados}


def mostra_dicionario(*args, **kwargs):
    print(f'nao nomeados {args}')

    for i,v in kwargs.items():
        print(i, v)


mostra_dicionario(21323, nome =  'arthur', n = 1234)

mostra_dicionario(**pessoa_completa)


