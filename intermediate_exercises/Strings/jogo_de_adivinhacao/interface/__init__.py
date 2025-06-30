"""
destinado a interface e mensagens na tela
"""
def _tracado(traco = '░') -> None:
    print(traco * 80)


def bem_vindo() -> None:
    _tracado()
    print('░','BEM VINDO AO JOGO DE ADIVINHACAO'.center(76),'░')
    _tracado()

def mensagem_sorteado(retorno):
    if retorno:
        return 'Voce acertou'
    if not retorno:
        return 'Voce errou'
