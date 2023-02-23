import math
num = int(input('Digite um numero entre 0 e 9999: '))
if num > 1000:
    m = num // 1000
    aux = m*1000
    num = num - aux
    c = num // 100
    aux = c*100
    num = num - aux
    d = num // 10
    aux = d*10
    num = num - aux
    u = num // 1
    print(f'Unidade - {u}\nDezena - {d}\nCentena - {c}\nMilhar - {m}')
"""elif num > 100:
    print(f'Unidade - {num[0]}\nDezena - {num[1]}\nCentena - 0\nMilhar - 0')
elif num > 10:
    print(f'Unidade - {num[0]}\nDezena - {num[1]}\nCentena - 0\nMilhar - 0')
else:
    print(f'Unidade - {num[0]}\nDezena - {num[1]}\nCentena - 0\nMilhar - 0')"""