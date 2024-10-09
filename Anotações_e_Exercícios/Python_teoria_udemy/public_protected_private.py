class Foo:
    def __init__(self):
        self.public = 'publico'
        self._protected = 'protegido'
        self.__private = 'privado'

    def metodo_publico(self):
        print('Método publico')
        self._metodo_protected()
        self.__metodo_private()
        print(self.public)
        print(self._protected)
        print(self.__private)
        
    
    def _metodo_protected(self):
        print('Método protegido')
        return 'Método protegido'
    
    def __metodo_private(self):
        print('Método privado')
        return 'Método privado'

f = Foo()
print(f.metodo_publico())
