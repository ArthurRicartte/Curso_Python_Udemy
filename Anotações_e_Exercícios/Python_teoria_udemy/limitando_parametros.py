def soma(a , b , / , *, x , y, **kwargs):
    print(kwargs)
    print(a + b + x + y)


soma(1, 3, x = 1, y = 2, nome = 'usopp')
print('^3^')