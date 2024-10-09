def executar(funcao, x):
    def pausar(y):
        return funcao(x,y)
    return pausar


def multiplicar(x,y):
    return x * y

multiplicar_por_10 = executar(multiplicar,10)

print(multiplicar_por_10(5))
print(multiplicar_por_10(2))
