"""
GAME: Pedra, Papel e Tesoura
Implemente um jogo onde o usuário escolhe pedra, papel ou tesoura, o computador também, e o programa decide quem venceu.

"""
from random import choice

def escolha_jogador():
    print('JOKENPO'.center(20))
    print('(1) pedra\n'
          '(2) papel\n'
          '(3) tesoura\n')

    escolha = int(input('escolha uma opcao: '))
    return escolha


def escolha_cpu():
    JOKENPO = ('pedra', 'papel', 'tesoura') # Variavel constante em maiuscula (PEP 8)
    sorteio = choice(JOKENPO)
    print(sorteio)


def comparar_jogada():
    if escolha_jogador() == 1 and escolha_cpu() == 'pedra':
        print('empatou')
    else:
        print('foi diferente')


comparar_jogada()