def notas(*n, situa=False):
    """
    Teste
    :param n:
    :param situa:
    :return:
    """
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n) / len(n)
    if situa:
        if r['Média'] >= 7:
            r['Situação'] = 'BOA'
        elif r['Média'] >= 5:
            r['Situação'] = 'RAZOÁVEL'
    else:
        r['Situação'] = 'RUIM'

    return r


#Programa Principal
resp = notas(2.3, 5.4, 8.0, 5, 7, 10.55, situa=True)
print(resp)
help(notas)