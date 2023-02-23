frase = str(input("Digite a frase: ")).replace(' ', '')
n = len(frase) - 1
aux = ''
for j in range(0, len(frase)):
    aux += frase[n]
    n -= 1
if frase == aux:
    print(f'A frase "{frase}" é um palindromo!')
else:
    print(f'A frase "{frase}" não é um palindromo!')
