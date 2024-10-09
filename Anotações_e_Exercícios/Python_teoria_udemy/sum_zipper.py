pares = [2,4,6,8,10]
impares = [1,3,5,7]
somatorio = []

def zipper_sum(l1, l2):
    limit = min(len(l1), len(l2))

    return[(l1[i]+l2[i])for i in range(limit)]


print(zipper_sum(pares, impares))

for i in range(min(len(pares), len(impares))):
    somatorio.append(pares[i] + impares[i])
#outra forma de fazer
print(somatorio)
