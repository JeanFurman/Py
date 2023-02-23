import random
nome1 = input('nome 1: ')
nome2 = input('nome 2: ')
nome3 = input('nome 3: ')
nome4 = input('nome 4: ')
r = [nome1, nome2, nome3, nome4]
print(f'O sorteado é {random.choice(r)}')
  