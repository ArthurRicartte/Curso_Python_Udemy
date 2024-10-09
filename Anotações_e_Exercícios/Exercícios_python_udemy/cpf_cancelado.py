import random

nove_digitos = ''
for i in range(9):
    nove_digitos += str(random.randint(0, 9))
contador_regressivo_1 = 10 
resultado_digito_1 = 0 



for n in nove_digitos:
    resultado_digito_1 += int(n) * contador_regressivo_1
    contador_regressivo_1 -= 1

primeiro_digito = resultado_digito_1 * 10 % 11

if primeiro_digito > 9:
    primeiro_digito = 0
else:
    primeiro_digito = primeiro_digito



dez_digitos = nove_digitos + str(primeiro_digito)

contador_regressivo_2 = 11
resultado_digito_2 = 0

for numero in dez_digitos:
    resultado_digito_2 += int(numero) * contador_regressivo_2
    contador_regressivo_2 -= 1

segundo_digito = resultado_digito_2 * 10 % 11

if segundo_digito > 9:
    segundo_digito = 0
else:
    segundo_digito = segundo_digito

cpf_programa = f'{nove_digitos}{primeiro_digito}{segundo_digito}'

print(cpf_programa)
