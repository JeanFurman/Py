import random
from time import sleep
n = random.randint(0, 5)
e = int(input('Escolha um numerode 0 a 5? '))
print('PROCESSANDO...')
sleep(3)
if n == e:
    print('Venceu!')
else:
    print(f'Perdeu! o certo era {n}')
