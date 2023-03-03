x = [1, 2, 3]
y = [4, 5, 6]

print(zip(x, y))
print(list(zip(x, y)))
print(list(zip('ABCD', 'xy')))

a = [1, 2, 3]
b = [4, 5, 6, 7, 8]

print(list(zip(a, b)))

d1 = {'a': 1, 'b': 2}
d2 = {'c': 4, 'd': 5}

print(list(zip(d1, d2)))
print(list(zip(d1, d2.values())))


def trocaValores(d1, d2):
    dicTemp = {}

    for d1key, d2val in zip(d1, d2.values()):
        dicTemp[d1key] = d2val

    return dicTemp


print(trocaValores(d1, d2))
