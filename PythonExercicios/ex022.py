nome = str(input('Qual seu nome: '))
letras = nome.replace(' ', '')
primeiro = nome.split()
primeiro = primeiro[0]
print(f'Upper - {nome.upper()}')
print(f'Lower - {nome.lower()}')
print(f'Letras - {len(letras)}')
print(f'Primeiro nome  - {len(primeiro)}')
