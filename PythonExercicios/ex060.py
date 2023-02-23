soma = n = int(input('Digite um numero: '))
string = f'{n} X '
for j in range(n-1, 0, -1):
    soma *= j
    aux = f'{j} X '
    string = string + aux
print(f'{n}! = {string[:len(string) - 2:]} = {soma}')
