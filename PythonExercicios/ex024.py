cidade = input('Nome da cidade: ').strip()
santo = cidade.split()

if santo[0].lower().find('santo') == 0:
    print('Começa')
else:
    print('Nao começa')
