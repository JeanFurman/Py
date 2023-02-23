palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar'
            , 'trabalhar', 'mercado', 'programador', 'futuro')
vogais = ('a', 'e', 'i', 'o', 'u')
frase = ''
for c in palavras:
    for j in vogais:
        for k in range(0, len(c)):
            if j == c[k]:
                frase += f'{j} '
    print(f'Na palavra {c.upper()} temos {frase}')
    frase = ''


