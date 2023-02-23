import random
cpu = random.randint(0, 10)
player = 11
palpites = 0
while player != cpu:
    player = int(input('Adivinhe o numero: '))
    palpites += 1
print(f'Voce acertou o numero! Porem precisou de {palpites} palpites!')
