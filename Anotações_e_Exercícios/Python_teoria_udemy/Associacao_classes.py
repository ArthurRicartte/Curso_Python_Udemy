class Escritor:
    def __init__(self, nome):
        self.escritor = nome
        self._ferramenta = None # só para usar assunto das outras aulas
    
    @property
    def ferramenta(self):
        print('Passando pelo getter')
        return self._ferramenta
    
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        print('Passando pelo setter')
        self._ferramenta = ferramenta
    

class FerramentaDeEscritor:
    def __init__(self, nome):
        self.nome = nome
    
    def escrever(self):
        return f'{self.nome} está escrevendo'

escritor = Escritor('Maria Letícia')
caneta = FerramentaDeEscritor('Caneta bic')

print(escritor.escritor)
print(caneta.escrever())

escritor.ferramenta = caneta #aqui é feita a conexão agora self.ferramenta passa a ser oq está em caneta
print(escritor.ferramenta.escrever()) #como a conexão foi  feita pode utilizar um método de FerramnentasEscritror

print()

one_piece = Escritor('Oda')
manga = FerramentaDeEscritor('caneta preta')

print(one_piece.escritor)
print(manga.escrever())

one_piece.ferramenta = manga
print(one_piece.ferramenta.escrever())#.ferramenta é o getter
