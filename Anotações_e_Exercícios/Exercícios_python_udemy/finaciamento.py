parcela = lambda montante, praz, tax: montante* ((1+tax)**praz * tax)/((1+taxa)**praz -1)

meses_possiveis = [6, 12, 18, 24,36]    

def porcento(prazo):    
    if prazo == 6:
        prazo = 0.07/12
    if prazo == 12:
        prazo = 0.1/12
    if prazo == 18:
        prazo = 0.12/12
    if prazo == 24:
        prazo = 0.15/12
    if prazo == 36:
        prazo = 0.18/12

    return prazo

while True:
    print('-*-' * 20)
    usuario = input('Digite seu nome:').strip()
    finaciamneto = float(input('Digite o valor do finaciamento:'))
    
    if finaciamneto == 0:
        break
    
    meses_prazo = int(input('deseja pagar em 6, 12, 18, 24 ou 36 vezes?'))
    if meses_prazo not in meses_possiveis:
        print('Mês inválido!')
        continue
    
    taxa = porcento(meses_prazo)
    parcela_mes = parcela(finaciamneto, meses_prazo, taxa)
   
    print(f'{usuario} irá pagar uma prestacao de R${parcela_mes:.2f} ao mês.')


print('cabou')
