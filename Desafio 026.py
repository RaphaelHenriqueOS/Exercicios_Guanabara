# Faça um programa que leia uma frase
f = str(input('Digite alguma coisa: ')).strip()
f = str(f.upper())
print('A letra A aparece: {}'.format(f.count('A')))
print('Ela aparece pela primeira vez em: {}'.format(f.find('A')))
print('Ela aparece pela última vez em: {}'.format(f.rfind('A')))