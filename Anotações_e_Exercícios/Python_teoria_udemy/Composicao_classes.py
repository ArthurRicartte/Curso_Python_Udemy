class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []
    
    def inserir_enderecos(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))#endereco interno
    
    def inserir_endereco_externo(self, endereco):#endereco externo
        self.enderecos.append(endereco)
    
    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)
    
    def __del__(self):#cor diferente uma função "pré programada" np python
        print('APAGANDO', self.nome)






class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero
    
    def __del__(self):#cor diferente uma função "pré programada" np python
        print('APAGANDO', self.rua, self.numero)


cliente1 = Cliente('Maria Letícia')
cliente1.inserir_enderecos('av brasail', 122)
cliente1.inserir_enderecos('Rua gregorio', 123)

endereco_externo = Endereco('av saudade', 455)
cliente1.inserir_endereco_externo(endereco_externo)#momento em que a composição de duas instâncias é feita

cliente1.listar_enderecos()
print()
del cliente1

print()
print(endereco_externo.rua, endereco_externo.numero)#é possível pois endereço_externo é uma instância de
#Endereco e não um atributo de cliente1


print('#FIM DO CÓDIGO#')
