times = ('Flamengo', 'Santos', 'Palmeiras', 'Gremio', 'Athletico PR', 'Sao paulo'
         , 'Internacional', 'Corinthians', 'Fortaleza', 'Goias', 'Bahia', 'Vasco', 'Atletico MG',
         'Fluminense', 'Botafogo', 'Ceara', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avai')

print('-=' * 30)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 30)
print(f'Os 5 primeiros times sao {times[0:5]}')
print('-=' * 30)
print(f'O 4 ultimos sao {times[-4:]}')
print('-=' * 30)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('-=' * 30)
print(f'O Chapecoense esta na {times.index("Chapecoense") + 1} posição')
