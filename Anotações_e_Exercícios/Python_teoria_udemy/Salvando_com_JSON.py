import json

pessoa = {'nome': 'Arthur Ricartte pereira polari',
          'altura': 1.68,
          'endereços': [
              {'rua': 'R1', 'número': 112421},
              {'rua': 'R2', 'número': 1346574784}
          ], 
          'casado?': True,
          'comida favorita': ('sushi', 'filé à parmegiana', 'pizza', 'torta de limão'), 
          'ídade': 17}


#para criar o arquivo e colocar o dicionário lá
with open('Salvando_com_JSON.json', 'w', encoding='utf8') as arquivo:
    json.dump(pessoa, arquivo, ensure_ascii=False, indent=2)
    

#Para ler o arquivo:
with open('Salvando_com_JSON.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa['nome'])
