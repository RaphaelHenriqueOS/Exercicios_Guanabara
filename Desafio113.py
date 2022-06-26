def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Tente novamente\033[m')
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Tente novamente\033[m')
        else:
            return n

num = leiaInt('Digite um número inteiro: ')
num2 = leiaFloat('Digite um número real: ')
print(f'O número digitado foi {num}')
print(f'\nO número digitado foi {num2}')