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


def resumo(p, a, r):
    print('-' * 30)
    print('{:^30}'.format('RESUMO DO VALOR'))
    print('-' * 30)
    print('{:<20}{:<}'.format('Preço analisado:', moeda(p)))
    print('{:<20}{:<}'.format('Dobro do preço:', dobro(p, True)))
    print('{:<20}{:<}'.format('Metade do preço:', metade(p, True)))
    print('{:<20}{:<}'.format('80% de aumento:', aumentar(p, a, True)))
    print('{:<20}{:<}'.format('35% de reduçao:', diminuir(p, r, True)))
    print('-' * 30)

