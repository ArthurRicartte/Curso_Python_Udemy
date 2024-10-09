class Pessoa:
    ano = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.a = 'oi' #serve para mostrar que o cls pode acessar os dados de init se usar self.idade dentro
        # do método da clase dá error
    
    @classmethod
    def saudar(cls):
        print('HEY')
    
    @classmethod #factories --> cria objetos sem precisar da instância
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)
    
    @classmethod #factories --> cria objetos sem precisar da instância
    def anonimo(cls, idade):
        return cls('Anônimo', idade)
    
    @classmethod
    def nomear(cls,usuario, idade):
        return cls(usuario, idade)

     


p1 = Pessoa('Maria Letícia', 18)
print(p1.nome, p1.idade)

p2 = Pessoa.criar_com_50_anos('João')
print(p2.nome, p2.idade) # se onservar, não temos idade em criar com 50 anos mas p2 consegue acessar o __init__
#e usar o atributo idade cls é como se fosse uma "extensão do self"

print(p2.a) # executa e mostra a informação que existe dentro de __init__

p3 = Pessoa.anonimo(43444)
print(p3.nome, p3.idade)

p4 = Pessoa.nomear('Maria Letícia', 130124)
print(p4.usuario)
print(p4.idade)
