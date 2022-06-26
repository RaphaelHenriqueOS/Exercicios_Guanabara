from time import sleep

def maior(* num):
    cont = 0
    print(f'\nO valor apresentado foi: ')
    for v in num:
        print(f'{num[cont]} -', end= ' ')
        cont += 1
        sleep(0.3)
    print(f'\nO maior valor apresentado foi {max(num)}.')

maior(2, 1, 7)
maior(4, 4, 7, 6, 2)
maior(8, 0)