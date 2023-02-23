nome = input('Seu nome: ').strip()
aux = nome.split()
print(f'Primeiro nome: {aux[0]}\nUltimo nome: {aux[len(aux)-1]}')
