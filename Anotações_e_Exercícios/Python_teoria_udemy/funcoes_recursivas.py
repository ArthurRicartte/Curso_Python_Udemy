def recursiva(inicio = 0, fim=10):
    #caso recursivo
    #contar até chegar no final
    if inicio >=fim:
        return fim
    #sem o if vai dar o stark overflow    
    inicio+=1
    
    return recursiva(inicio, fim)


print(recursiva())

def factorial(n):
    if n <= 1:
        return 1 # fatorial de 1 ou 0 é 1 e não existe fatorial de negativos
    
    return n * factorial(n-1)

print(factorial(5))
print(factorial(1000))#Stack Overflow
