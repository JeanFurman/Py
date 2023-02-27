def metade(p, t):
    return moeda(p/2) if t else p/2


def dobro(p, t):
    return moeda(p * 2) if t else p * 2


def aumentar(p, n, t):
    p += p*n/100
    return moeda(p) if t else p


def diminuir(p, n, t):
    p -= p * n / 100
    return moeda(p) if t else p


def moeda(p):
    return str(f'R${p:.2f}')
