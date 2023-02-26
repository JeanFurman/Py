def fatorial(n, show=False):
    print('-' * 20)
    p = n
    for k in range(1, n):
        n *= k
    if show:
        for o in range(p, 0, -1):
            if o == 1:
                print(f'{o} = ', end='')
            else:
                print(f'{o} x ', end='')

    return n


print(fatorial(6, True))
