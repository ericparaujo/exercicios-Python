"""
GAME: Pedra, Papel e Tesoura
Implemente um jogo onde o usuário escolhe pedra, papel ou tesoura, o computador também, e o programa decide quem venceu.

"""
from random import choice


def escolha_jogador(escolha):
    print(escolha)
    return escolha


def escolha_cpu():
    _JOKENPO = ('pedra', 'papel', 'tesoura') # Variavel constante em maiuscula (PEP 8)
    sorteio = choice(_JOKENPO)
    print(sorteio)
    return sorteio



def comparar_jogada():
    sorteio = escolha_cpu()
    minha_escolha = escolha_jogador()

    if minha_escolha == sorteio:
        print('empatou')
    elif minha_escolha == 'pedra' and sorteio == 'papel':
        print('voce perdeu')
    elif minha_escolha == 'pedra' and sorteio == 'tesoura':
        print('voce ganhou')
    elif minha_escolha == 'papel' and sorteio == 'pedra':
        print('voce ganhou')
    elif minha_escolha == 'papel' and sorteio == 'tesoura':
        print('voce perdeu')
    elif minha_escolha == 'tesoura' and sorteio == 'pedra':
        print('voce perdeu')
    elif minha_escolha == 'tesoura' and sorteio == 'papel':
        print('voce ganhou')




if __name__ == '__main__':
    comparar_jogada()