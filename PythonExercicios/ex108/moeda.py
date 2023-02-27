def metade(p):
    return p/2


def dobro(p):
    return p * 2


def aumentar(p, n):
    return p + (p*10/100)


def diminuir(p, n):
    return p - (p * 13 / 100)


def moeda(p):
    return str(f'R${p:.2f}'. replace('.', ','))
