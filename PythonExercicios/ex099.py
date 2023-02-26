def maior(*n):
    print('-=' * 30)
    print('Analisando valores passados...')
    for k in n:
        print(f'{k} ', end='')
    print(f'Foram informado {len(n)} valores ao todo.')
    print(f'O maior valor informado foi {max(n) if n != () else 0}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

