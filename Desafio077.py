palavras = ('casa', 'escola', 'vaso', 'furadeira', 'onibus', 'carro', 'estudar', 'dançar',
            'vacina', 'torre', 'comer', 'sacada', 'faxinar', 'caderno', 'aviao', 'otorrino')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

