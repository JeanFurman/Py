def ficha(nome='', gols=0):
    print('O jogador ', end='')
    print(f'<desconhecido> ' if nome == '' else f'{nome} ', end='')
    print(f'fez {gols} gol(s) no campeonato.')


print('-' * 30)
nome = str(input('Nome do Jogador: '))
gols = input('Numero de gols: ')
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0


ficha(nome, gols)
