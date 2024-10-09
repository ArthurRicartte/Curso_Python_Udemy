def e_string(parametro):
    if not isinstance(parametro, str):
        raise TypeError('parametro só pode ser string.')
    
def executa(funcao):
    print(f'Vou decorar')
    
    def interno(*args, **kwargs):#foi colocado ** só por cololcar mesmo pois não é posível colocar 
        for arg in args:         #argumentos nomeados no inverte_parametro
            e_string(arg)
        resultado = funcao(*args, **kwargs)     
       
        print(f'Resultado: {resultado}')
        print('Já decorada.')
        return resultado
    
    return interno

@executa #Syntax sugar
def inverte(string):
    return string[::-1]


print(inverte('Arthur'))
