
palavra_secreta = 'perfume'
letras_acertadas = ''
tentativas = 0
while True:

    letra = input('Digite uma letra:').strip()

    if not letra:
        print('Error digite só uma letra')
        continue
    elif len(letra) > 1:
        print('Erro digite só uma letra')
        continue
    
    tentativas += 1
    if letra in palavra_secreta:
        letras_acertadas += letra
    
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print(f'Palavra formada: {palavra_formada}')

    if palavra_formada == palavra_secreta:
        print('PARABENS')
        print(f'A palavra era: {palavra_secreta}')
        print(f'tentativas: {tentativas}')
        break
print('fim')



