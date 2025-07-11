def bem_vindo():
    print(f'{cores('amarelo')}╔{'═' * 78}╗')
    print('║', f'{cores('vermelho')}SISTEMA DE APROVACAO DE EMPRESTIMO{cores('amarelo')}'.center(86), '║')
    print(f'╚{'═' * 78}╝{cores('limpar')}')


def cores(tinta):
    """
    muda a cor das fontes
    :param tinta: destinada a cor a qual se quer mudar
    :return:
    """
    paleta = {'vermelho':'31m',
              'verde':'32m',
              'amarelo':'33m',
              'azul':'34m',
              'limpar':'m'
              }
    cor = f'\33[{paleta[tinta]}'
    return cor
