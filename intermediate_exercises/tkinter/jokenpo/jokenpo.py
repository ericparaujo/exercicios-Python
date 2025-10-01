"""
GAME: Pedra, Papel e Tesoura
Implemente um jogo onde o usuário escolhe pedra, papel ou tesoura, o computador também, e o programa decide quem venceu.

"""
from random import choice
from interface import painel_principal

def escolha_cpu():
    escolha_random = choice(("pedra", "papel", "tesoura"))
    return escolha_random


def minha_escolha():
    painel_principal()
    escolha = painel_principal()
    return escolha
'''
    if escolha == 1:
        escolha = 'pedra'
    elif escolha == 2:
        escolha = 'papel'
    elif escolha == 3:
        escolha = 'tesoura'
    else:
        print('opcao invalid, tente novamente')
'''






print(minha_escolha())