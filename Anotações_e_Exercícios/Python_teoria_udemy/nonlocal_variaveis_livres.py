def concatenar(string_inicial):
    valor_final = string_inicial

    def interno(string_manipulada):
        nonlocal valor_final
        valor_final += string_manipulada
        return valor_final
    return interno


c = concatenar('a')

print(c('b'))
print(c('c'))
print(c('d'))
final = c('')
print(final)

