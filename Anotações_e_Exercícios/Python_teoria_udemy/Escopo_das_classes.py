class Animal:
    #leao = 'leão' ---> é posível fazer isso e chamar sem o self! tipo animal(leao)

    def __init__(self, nome): 
        self.nome = nome

        variavel = 'Valor'
        print(variavel)

    def comendo(self, comida):
        return f'{self.nome} está comendo {comida}'
    
    def executar(self, *args, **kwargs): # se quiser usar o kwargs tem que colcoar **comida na linha 10    
        return self.comendo(*args, **kwargs) #sempre que for usar o self ele tem que vim primeiro depois um ponto
        #e o método


magago = Animal('monkey')
print(magago.nome)
print(magago.executar('banana'))
