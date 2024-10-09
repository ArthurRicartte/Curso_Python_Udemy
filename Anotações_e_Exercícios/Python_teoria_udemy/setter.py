class Caneta:
    def __init__(self, cor):
        self._cor = cor #esse _ no início significa que não é para chama-ló fora da classe
        self._cor_tampa = None

    
    @property
    def cor(self):
        print('ESTOU NO PROPERTY')
        return self._cor
    
    @cor.setter #não funciona sem o getter(@property)
    def cor(self, valor):
        print('ESTOU NO SETTER')
        self._cor = valor
    
    @property
    def cor_tampa(self):
        print('ESTOU NO PROPERTY')
        return self._cor_tampa
    
    
    @cor_tampa.setter #não funciona sem o getter(@property)
    def cor_tampa(self, valor):
        print('ESTOU NO SETTER')
        self._cor_tampa = valor


bic = Caneta('Azul')
bic.cor = 'roxo' #setter
bic.cor_tampa = 'preta' #setter
print()
print(bic.cor) #getter
print(bic.cor_tampa) #getter
