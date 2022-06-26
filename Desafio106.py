def ajuda():
    from time import sleep
    while True:
        texto = "\033[42mSistema de Ajuda do PyHelp"
        texto2 = "\033[44mAcessando Manual de Comando"
        tam = len("Sistema de Ajuda do PyHelp") + 4
        print('\033[42m-' * tam)
        print(f'  {texto}')
        print('\033[42m-' * tam)
        print('\033[m')

        msg = (str(input('Função ou Biblioteca > ')))

        print('\033[44m-' * tam)
        print(f'Acessando Manual de Comando {msg}')
        print('\033[44m-' * tam)
        print('\033[m')

        sleep(1.0)
        print('\033[30;107m')
        help(msg)
        print('\033[m')
        if ajuda == 'FIM':
            print('\033[45m')
            help(msg)
            print('\033[m')
            break
        break


ajuda()

