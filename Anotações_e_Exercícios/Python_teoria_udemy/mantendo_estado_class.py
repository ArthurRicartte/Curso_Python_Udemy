class Camera:
    def __init__(self, nome, filmando=False, fotografar = False):
        self.nome = nome
        self.filmando = filmando
        self.fotografando = fotografar
    
    def filmar(self):
        if self.fotografando:
            print(f'{self.nome} não pode filmar tirando fotos')
            return
        elif self.filmando:
            print(f'{self.nome} já está filmando...')
            return
        
        print(f'{self.nome} está filmando...')
        self.filmando = True

    def parar_filmar(self):
        if not self.filmando or self.fotografando:
            print(f'{self.nome} não está filmando...')
            return
        
        print(f'{self.nome} está parando de filmar...')
        self.filmando = False

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar filmando...')
            return
        elif self.fotografando:
            print(f'{self.nome} já está fotografando')
            return
    
        
        print(f'{self.nome} está fotografando...')
        self.fotografando = True

    def parar_fotos(self):
        if not self.fotografando or self.filmando:
            print(f'{self.nome} não está tirando fotos...')
            return
        print(f'{self.nome} está parando de fotografar....')
        self.fotografando = False

#Como esses métodos estão dentro do escopo da classe, pode guardar estados das funções e consequentemente do obj
c1 = Camera('Sony')

c1.filmar()
c1.filmar()
c1.fotografar()
c1.parar_filmar()
c1.fotografar()
c1.filmar()
c1.parar_fotos()
c1.parar_fotos()
c1.filmar()
c1.parar_fotos()

# c1.filmando() -> se fizesse isso por engano ia dizer que bool não é calablle pois calablle é um objeto que
#pode ser chamado e filmando é um atributo e não pode ser chamado com ()

#teste para ver se o código funciona -> funcionou! -> AMO MEU AMOR (MARIA LETÍCIA BRITO POLARI) vou casar com ela
