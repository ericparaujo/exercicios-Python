"""
Sorteando um item na lista: faça um programa que leia vários nomes e escolha aleatoriamente um deles para ser o “sortudo”
"""

from random import choice

def solicitar_usuario() -> str:
    """
    solicita a entada com o nome do usuario a ser incluido na lista para ser sorteada.
    :return:
    """
    nome = str(input('Digite um nome: ')).strip().upper()
    return nome


def deseja_continuar() -> bool:
    """
    pergunta se o usuario quer continuar ou nao.
    :return:
    """
    while True:
        continuar = str(input('Deseja Continuar [S/N]: ')).strip().upper()[0]
        if continuar == 'S':
            return True
        if continuar == 'N' or continuar == '':
            return False
        print('Opcao invalida, tente novamente')


def sortear_nome(nome: list[str]) -> str:
    """
    sorteia um nome de forma aleatoria
    :param nome:
    :return:
    """
    return choice(nome)


def entrada_dados() -> None:
    """
    Controla o fluxo principal do programa:
    - Solicita nomes ao usuário até que ele decida parar.
    - Armazena os nomes em uma lista.
    - Exibe a lista completa de nomes.
    - Sorteia e exibe um nome "sortudo" da lista.
    - Caso nenhum nome seja inserido, exibe mensagem apropriada.

    :return:
    """
    nomes: list[str] = []
    while True:
        nomes.append(solicitar_usuario())
        if not deseja_continuar():
            break

    if nomes:
        print(f'lista de nomes: {nomes}')
        print(f'nome sorteado: {sortear_nome(nomes)}')
    else:
        print('nenhum nome foi inserido')


if __name__ == '__main__':
    entrada_dados()
