from random import randint
from time import sleep
competidores = [{'nome': 'player1', 'valor': 0}, {'nome': 'player2', 'valor': 0},
                {'nome': 'player3', 'valor': 0}, {'nome': 'player4', 'valor': 0}, ]
ordem = []
maior = 0
print('Valores sorteados: ')
for c in competidores:
    c['valor'] = randint(1, 6)
    print('{:^23}'.format(f' O {c["nome"]} tirou {c["valor"]}'))
    sleep(0.5)
print('Ranking dos jogadores:')
for c in range(0, 4):
    if c == 0:
        ordem.append(competidores[c].copy())
    else:
        aux = 0
        for o in range(0, len(ordem)):
            n = ordem[o]['valor']
            if competidores[c]['valor'] >= n:
                ordem.insert(o, competidores[c].copy())
                break
            else:
                aux += 1
        if aux == len(ordem):
            ordem.append(competidores[c].copy())
for o in range(0, len(ordem)):
    print('{:^27}'.format(f' {o + 1} lugar: {ordem[o]["nome"]} com {ordem[o]["valor"]}'))
    sleep(0.5)

'''from random import randint
from time import sleep

jogos1 = {}
c = 1

for cont in range(1, 5):
    jogada = randint(1, 6)
    jogos1["jogador" + str(cont)] = jogada
print('Valores sorteados:')
for k, v in jogos1.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
print('-=' * 30)
print(f'{"== RANKING DOS JOGADORES ==":^30}')
jogos2 = dict(sorted(jogos1.items(), key=lambda item: item[1], reverse=True))
for k, v in jogos2.items():
    print(f'{c}o. lugar: {k} com {v}.')
    c +=1
    sleep(1)'''