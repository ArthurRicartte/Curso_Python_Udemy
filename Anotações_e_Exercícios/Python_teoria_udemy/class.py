class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('Maria letica brito', 'polari')
p2 = Pessoa('One', 'Piece')

print(p1.nome)
print(p1.sobrenome)
print(p2.nome)
print(p2.sobrenome)
print()

#Métodos em instâncias de classes python:

class Carro:
    def __init__(self, nome):
        self.nome = nome #aqui de certa forma você define os atributos do objeto essa função é obrigatória!
        #para utilizar o self em outras funções no caso métodos!
    
    def acelerar(self):#esse self é diferente do self do __init__
        print(f'{self.nome} está acelerando... vrumm vrummm') #ambos os selfs se referem a mesma coisa mas em
        #funções diferentes então nessa função acelerar quando digita self.nome ele já entende que está falando
        #de um atributo da instância chamado nome  


supra = Carro('Supra')
supra.acelerar()
