class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property
    def cor(self): #se comporta como um atributo, mas é um método, é tecnicamente um getter
        print('aaaaaa')
        return self.cor_tinta
    

    def get_cor(self): # é um getter 
        return self.cor_tinta

pen = Caneta('Azul')
print(pen.cor)# essa execução está certa
print(pen.cor)
print(pen.cor)
print(pen.cor)
print(pen.cor)
print(pen.cor)
# se no código cliente (código de outras pessoas que usam seu código) tiver várias linhas que chamem a cor caneta
#elas podem acessar a cor_tinta por meio do "método" cor e isso permite alterções livremente no código sem dar
#erro no código cliente