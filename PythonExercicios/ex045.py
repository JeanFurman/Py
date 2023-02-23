import random
import time
user = int(input('Escolha 1 para pedra, 2 para papel, 3 para tesoura: '))
cpu = random.randint(1, 3)
winU = False
winC = False

if user == 1 and cpu == 3:
    winU = True
elif user == 2 and cpu == 1:
    winU = True
elif user == 3 and cpu == 2:
    winU = True
elif cpu == 1 and user == 3:
    winC = True
elif cpu == 2 and user == 1:
    winC = True
elif cpu == 3 and user == 2:
    winC = True

if winU or winC:
    print('CALCULANDO....')
    time.sleep(3)
    if winU:
        print('Parabens, voce venceu!')
    else:
        print('Voce perdeu!')
else:
    print('CALCULANDO....')
    time.sleep(3)
    print('Deu empate!')

print(f'Cpu - {cpu} / User - {user}')