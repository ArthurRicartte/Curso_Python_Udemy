def fabrica_decoradores(nome):
    def funcao_decoradora(func):
        print('Decorador:', nome)
        def sua_nova_funcao(*args, **kwargs):
            res = func(*args, **kwargs) #tem q manipular para recebr mais de um argumento -> tratar um tupla 
            final = f'{res} {nome}'
            return final 
        return sua_nova_funcao
    return funcao_decoradora


#se tiver dúvida usa o debug!
@fabrica_decoradores(5)
@fabrica_decoradores(4)
@fabrica_decoradores(3)
@fabrica_decoradores(2)
@fabrica_decoradores(1)
def soma(x, y):
    return x + y


print(soma(12,1))
