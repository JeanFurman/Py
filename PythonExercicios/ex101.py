from datetime import date


def voto(ano):
    if idade < 16:
        return 'NAO VOTA'
    if 16 <= idade < 18 or idade > 65:
        return 'VOTO OPCIONAL'
    else:
        return 'VOTO OBRIGATORIO'


print('-' * 25)
idade = date.today().year - int(input('Em que ano voce nasceu? '))
print(f'Com {idade} anos: {voto(idade)}.')