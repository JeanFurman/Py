jogador = {}
jogador['nome'] = str(input('Nome do Jogador: '))
n = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
jogador['gols'] = list()
soma = 0
for a in range(0, n):
    jogador['gols'].append(int(input(f'Quantos gols na partida {a}? ')))
    soma += jogador['gols'][a]
jogador['total'] = soma
print('-=' * 40)
print(jogador)
print('-=' * 40)
for x, y in jogador.items():
    print(f'O campo {x} tem o valor {y}.')
print('-=' * 40)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for g in range(0, len(jogador['gols'])):
    print('{:>32}'.format(f'=> Na partida {g}, fez {jogador["gols"][g]} gols.'))
print(f'Foi um total de {jogador["total"]} gols.')
