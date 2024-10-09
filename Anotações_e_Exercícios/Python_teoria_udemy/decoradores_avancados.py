def fabrica_de_decoradores(a = None, b = None, c = None):
    print('crinado a função decoradora',a,b,c)

    def fabrica_de_funcao(func):
        print('função criada.')

        def aninhada(*args, **kwargs):
            res = func(*args, **kwargs)

            return res
        return aninhada
    return fabrica_de_funcao


@fabrica_de_decoradores(1,2,3)
def soma(x,y):
    return x + y

print(soma(12,1))
