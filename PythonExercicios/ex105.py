def notas(*num, sit=False):
    """
    ->Funçao para analisar notas e situaçoes de varios alunos.
    :param num: uma ou mais notas dos alunos (aceita varias)
    :param sit: valor opcional, indicando se deve ou nao adicionar a situaçao
    :return: dicionario com varias informaçoes sobre a situaçao da turma
    """
    d = dict()
    d['total'] = len(num)
    d['maior'] = max(num)
    d['menor'] = min(num)
    d['media'] = sum(num)/d['total']
    if sit:
        if d['media'] >= 7:
            d['situacao'] = 'BOA'
        elif d['media'] >= 5:
            d['situacao'] = 'RAZOAVEL'
        else:
            d['situacao'] = 'RUIM'
    return d


print('-' * 30)
resp = notas(3.5, 10, 6.5, sit=True)
print(resp)
help(notas)
