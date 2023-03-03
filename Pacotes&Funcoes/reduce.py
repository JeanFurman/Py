from functools import reduce

lista = [47, 11, 42, 13]
print(lista)


def soma(a, b):
    x = a+b
    return x


print(reduce(soma, lista))
lst = [47, 11, 42, 13]
lststr = ['abc', 'def', 'ghi', 'jkl']
print(reduce(lambda x, y: x+y, lst))
max_find2 = lambda a, b: a if (a > b) else b
print(type(max_find2))
print(reduce(max_find2, lst))
print(reduce(max_find2, lststr))
