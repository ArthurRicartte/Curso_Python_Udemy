import json

CAMINHO_ARQUIVO = 'salvando_classes.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    


p1 = Pessoa('Maria Letícia Brito Polari', 18)
p2 = Pessoa('Luffy', 19)
p3 = Pessoa('Ussop', 19)

lista = [vars(p1), p2.__dict__, vars(p3)] #é necessário o vars ou o dict pois o arquivo não reconhece a classe


def fazendo_dump(): # é necessária essa função pois quando esse arquivo é importado 
    print('Fazendo dump') #o dump seria feito automaticamente então essa função serve para adiar a execução
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo:
        json.dump(lista, arquivo, ensure_ascii= False, indent=2)



if __name__ == '__main__':# se qualquer coisa fosse printada no escopo global de A ou até uma função 
    print('O arquivo A é o main') # seria executado em B por isso esse if 'w importante para evitar isso
    fazendo_dump()

#print('AAAA') se quiser testar apaga esse if acima faz esse print e executa o B