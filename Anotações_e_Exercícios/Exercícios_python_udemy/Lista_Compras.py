compras = []
possibilidades = ('d', 'a', 'l', 's')
while True:
    print('-*-' * 20)
    print('DELETAR[d] ADICIONAR[a] LISTAR[l] SAIR[s]')
    choice = input('Sua escolha:').lower().strip()

    if not choice:
        print('ERROR DIGITE!')
        continue
    elif choice not in possibilidades: 
        print('ERROR DIGITE UMA OPÇÃO VÁLIDA!')
        continue
    
    else:
        indice = ''
        if choice == 'a':
            add = input('Qual produto gostaria de adicionar?').strip()
            if not add:
                print('ERROR')
                continue 

            else:
                compras.append(add)
        
        elif choice == 'd':
            indice = int(input('Digite o índice do produto:'))
            try:
                print(f'Produto deletado {compras[indice]}')
                del(compras[indice])
            except IndexError:
                print('ERROR ÍDICE INEXISTENTE.')
                continue
            
                
        elif choice == 'l':
            if len(compras) == 0:
                print('NADA A MOSTRAR')
            for i, v in enumerate(compras):
                print(i, v)
        else:
            break

print(compras)
print('BOAS COMPRAS')

