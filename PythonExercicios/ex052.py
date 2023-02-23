n = int(input('Digite um numero: '))
primo = True
for j in range(2, n):
    if (n // j) < j:
        break
    if n % j == 0:
        primo = False
        break

if primo:
    print(f'O numero {n} é primo!')
else:
    print(f'O numero {n} não é primo!')