#A padaria Sópão vende diariamente uma certa quantidade de pães franceses e uma quantidade de broas. 
#Cada pãozinho custa R$ 0,80 e a broa custa R$ 2,50. Do total da arrecadação, 43% correspondem aos 
#custos de fabricação. Do restante, Seu João guarda 15% numa conta de poupança e 15% ele converte em 
#Euros para sua viagem anual. Sabe-se que 1 Euro custa R$ 4,60. Com base nestes fatos, faça um programa 
#para ler as quantidades de pães e de broas, calcule a venda total de pães e broas
#, o custo de fabricação, quanto irá economizar na poupança e quantos euros irá comprar. 
#Ao final exibir os dados calculados.

paozim = int(input('Quantos pães foram vendidos?'))
broazinha = int(input('Quantas broas foram vendidas?'))

valor_arrecadado_pao = paozim*0.8
valor_arrecadado_broa = broazinha * 2.5

valor_total_arrecadado = valor_arrecadado_broa + valor_arrecadado_pao

lucro_obtido = valor_total_arrecadado * 0.57
custo_producao = valor_total_arrecadado * 0.43

poupanca = valor_viagem = lucro_obtido * 0.15

euro = valor_viagem / 4.60

valor_restante = lucro_obtido * 0.70

print('Dados')
print(f'pães vendidos R${paozim:.2f}')
print(f'Broas vendidas R${broazinha:.2f}')
print(f'Valor de venda dos pães: R${valor_arrecadado_pao:.2f}')
print(f'Valor de venda das broas: R${valor_arrecadado_broa:.2f}')
print(f'valor total arrecadado R${valor_total_arrecadado:.2f}')
print(f'custo de produção: R${custo_producao:.2f}')
print(f'Lucro obtido: R${lucro_obtido:.2f}')
print(f'Poupança: R${poupanca:.2f}')
print(f'Viagem: R${valor_viagem:.2f}')
print(f'Euros: R${euro:.2f}')
print(f'valor restante R${valor_restante:.2f}')


