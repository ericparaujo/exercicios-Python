def formula_imc():
    imc = peso / (altura ** 2)
    return imc


def cores():
    return {
        'limpar': '\033[m',
        'preto': '\033[1;47;30m',
        'vermelho': '\033[31m',
        'verde': '\033[32m',
        'amarelo': '\033[33m',
        'azul': '\033[1;34m',
        'magenta': '\033[35m',
        'ciano': '\033[36m',
        'cinza': '\033[37m',
        'branco': '\033[97m'
        }


def tabela_imc(imc):
    if imc < 17:
        return 'esta muito abaixo do peso', cores()['vermelho']
    elif imc <= 18.49:
        return 'esta abaixo do peso', cores()['amarelo']
    elif imc <= 24.99:
        return 'esta com o peso normal', cores()['verde']
    elif imc <= 29.99:
        return 'esta acima do peso', cores()['amarelo']
    elif imc <= 34.99:
        return 'esta com OBESIDADE NIVEL I', cores()['vermelho']
    elif imc <= 39.99:
        return 'esta com obesidade nivel II (severa)', cores()['magenta']
    else:
        return 'esta com OBESIDADE III (mórbida)        ', cores()['preto']


opcao = 'S'
limpar = cores()['limpar']

while True:
    if opcao == 'S':
        print(f'{cores()["ciano"]}█' * 69)
        print(f'{"█":<68}''█'
              f'\n█ {cores()["azul"]}{"BEM VINDO AO SISTEMA DE CONTROLE DE PESO":^65}'f'{cores()["ciano"]} █'
              f'\n{"█":<68}''█')
        print('█' * 69, '\n\n')

        peso = float(input(f'{limpar}qual é seu peso? '))
        altura = float(input('qual a sua altura? '))

        formula = formula_imc()
        tabela, cor = tabela_imc(formula_imc())

        print(f'\n{cor}seu indice de massa corporal (IMC) é de {formula:.2f}{limpar}')
        print(f'{cor}Você {tabela}{limpar}')
        opcao = str(input('\n\ndeseja repetir: [S/N]\n\n')).strip().upper()

    elif opcao == 'N':
        print('obrigado por usar o sistema IMC.'
              'VOLTE SEMPRE')
        break
    else:
        print('A opcao digitada nao existe. Tente novamente.')
        opcao = str(input('deseja repetir: [S/N]\n\n')).strip().upper()
