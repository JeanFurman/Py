def verificarPar(num):
    if num % 2 == 0:
        return True
    else:
        return False


print(verificarPar(35))
print(verificarPar(10))
lista = []
for l in range(0, 19):
    lista.append(l)
print(lista)
print(filter(verificarPar, lista))
print(list(filter(verificarPar, lista)))
print(list(filter(lambda x: x % 2 == 0, lista)))
print(list(filter(lambda num: num > 8, lista)))
