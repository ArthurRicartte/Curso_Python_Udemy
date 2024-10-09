import json
from Salvando_Classes_A import CAMINHO_ARQUIVO, Pessoa, fazendo_dump

fazendo_dump()# serve mais para ajudar a explicar que se apagar um dado no arquiv.json o print p3(ex)
#pode dar error sem essa função não consegue explicar que pode dar error pq como importa p A tudo dele executa
# no B, inclusive o dump

with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo:
    pessoas = json.load(arquivo)
    
    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    p3 = Pessoa(**pessoas[2])
    
    print(p1.nome, p1.idade)
    print(p2.nome, p2.idade)
    print(p3.nome, p3.idade)

print(__name__)
