def leiaDinheiro(s):
    while True:
        p = str(input(s))
        aux = p
        if aux.replace('.', '', 1).replace(',', '', 1).isdigit():
            return float(p.replace(',', '.'))
        else:
            print(f'\033[31mERRO: "{p}" é um preço invalido!\033[m')
