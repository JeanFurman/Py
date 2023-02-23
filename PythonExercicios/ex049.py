n = int(input('Escolha um numero: '))

print(':=#' * 5)
for j in range(0, 11):
    print(f'| {n} X {j} = {j*n} |')
print(':=#' * 5)