def nao_podi_zero(b):
    if b == 0:
        raise ZeroDivisionError('n pode dividir por zero')
    return True

def so_int_float(n):
    tipo = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(f'"{n}" deve ser int ou float'
                        f'"{tipo.__name__}" enviado'
        )

    return True

def divide(a,b):
    so_int_float(a)
    so_int_float(b)
    nao_podi_zero(b)
    return a/b


print(divide(1,0))
