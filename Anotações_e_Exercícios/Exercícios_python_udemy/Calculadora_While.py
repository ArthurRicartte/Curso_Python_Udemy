from time import sleep

def linhas_frufru(text):
    sleep(1)
    print('𒉭'*10)
    sleep(0.9)
    print(text)
    sleep(0.8)
    print('𒉭'*10)
    


while True:
    print('-*-' * 14)
    print('CALCULADORA WHILE')
    print('-*-' * 14)
    sleep(1)
    print('Multiplicação[x]')
    sleep(0.9)
    print('Divisão[/]')
    sleep(0.8)
    print('Soma[+]')
    sleep(0.7)
    print('Subtração[-]')
    sleep(0.6)
    print('Sair do programa[s]')
    sleep(0.5)
    print('-*-' * 14)
    sleep(0.4)
    opcoes = ['x', '/', '+', '-', 's']
    sleep(0.9)
    
    choice = input('Qual opereção deseja fazer:').strip().lower()

    sleep(0.8)
    if choice not in opcoes:
        print('ERROR OPÇÃO INVÁLIDA.')
        continue
    elif choice == opcoes[4]:
        for i in range(3, 0, -1):
            print(f'saindo em {i}')
            sleep(1)

        break

    else:
        try:
            n1 = int(input('Primeiro numero:'))
            sleep(0.8)
            n2 = int(input('Segundo número:'))
            sleep(0.8)
        except ValueError:
            print('errornsónumero')
            continue
    


    sleep(0.8)
    if choice == opcoes[0]:
        linhas_frufru(f'{n1} x {n2} = {n1*n2}')
        
    elif choice == opcoes[1]:
        linhas_frufru(f'{n1} / {n2} = {n1/n2}')
        
    elif choice == opcoes[2]:
        linhas_frufru(f'{n1} + {n2} = {n1+n2}')

    elif choice == opcoes[3]:
        linhas_frufru(f'{n1} - {n2} = {n1-n2}')
        
    
print('SALA MALEICO')


                
