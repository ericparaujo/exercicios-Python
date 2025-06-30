"""
destinado a funçao principal do programa
"""
from exercicios2.jogo_de_adivinhacao.interface import *
from random import randint


def minha_escolha() -> int:
    bem_vindo()
    while True:
        try:
            meu_numero = int(input('\n''Escolha um numero de 0 a 5: '))
        except ValueError:
            print('entrada invalida! tente novamente apenas com numeros')
            continue

        if not 0 <= meu_numero <= 5:
            print('Opcao invalida, tente novamente')
            continue

        return meu_numero


def comparar_sorteio() -> bool:
    sorteio = randint(0, 5)
    if sorteio != minha_escolha():
        return False
    else:
        return True


def mostrar_resultado() -> None:
    if comparar_sorteio() is True:
        print(mensagem_sorteado(True))

    else:
        (print(mensagem_sorteado(False)))


def deseja_confinuar(continuar='S') -> None:
    while True:
        mostrar_resultado()
        continuar = str(input('deseja continuar [S/N]: ')).strip().upper()
        if continuar not in ('S', 'N'):
            print('entrada invalida, tente novamente')
            continue

        if continuar == 'N':
            print('obrigado por jogar comigo')
            break
        #continue


