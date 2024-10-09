frase = 'O Python é uma linguagem de programação multiparadigma criada por Guido Van Rossum.'

i = 0

qtd_mais_vezes = 0
letra_mais_vezes = ' '

while i < len(frase):
    letra_atual = frase[i]
    

    if letra_atual == ' ':
        i += 1
        continue
    
    qtd_atual = frase.count(letra_atual)
    
    if qtd_mais_vezes < qtd_atual:
        letra_mais_vezes = letra_atual
        qtd_mais_vezes = qtd_atual
    
    i += 1

print(f'Apareceu mais vezes: {letra_mais_vezes} == {qtd_mais_vezes} vezes.')

