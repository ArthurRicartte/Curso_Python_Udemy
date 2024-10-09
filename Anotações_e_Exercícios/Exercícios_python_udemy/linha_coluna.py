linhas = 4
colunas = 4


linha = 1

while linha <= linhas:
    coluna = 0
    
    while coluna < colunas:
        coluna += 1 
        print(linha, '=', coluna)

    linha += 1

print('cabou')
