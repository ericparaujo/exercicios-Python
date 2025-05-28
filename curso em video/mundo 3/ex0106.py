def Comando(cmd):
    def mensagem(msg):
        print('')
    while True:
        print(f'\033[97;44m',
              f'{"BEM VINDO AO SISTEMA DE HELP":^100}{"":50}',
              '\033[m')
        cmd = input(f'digite um comando: ').strip()

        if cmd == 'fim':
            print('fechando o sistema de help')
            break

        else:
            print(f'\033[31;107m',
                  f'{help(cmd)}',
                  f'\033[m')


comando = str
Comando(comando)
