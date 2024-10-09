def par_impar(num):
    if num % 2 == 0:gt
    return f'{num} é par'
    return f'{num} é ímpar'



while True:
    number_choice = int(input('Qula número vc deseja verificar?'))
    print(par_impar(number_choice))
    
    choice = input('Deseja sair?[S] ou [N]').strip().upper()

    if choice == 'N':
        print('OK CONTINUANDO...')
    elif choice == 'S':
        break
    else:
        print('OPÇÃO INVÁLIDA')
    
    print('-*-' *10)

print('cabou')
  