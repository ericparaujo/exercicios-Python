"""
destinado a interface
"""

from exercicios2.custoDeViagem.interface.cores import vermelho, apagar, amarelo

def tracado(traco = '='):
    return traco * 79


def bem_vindo():
    print(f'{amarelo()}{tracado()}{apagar()}')
    print(f'{vermelho()}Bem vindo ao sistema de controle de custo por viagem{apagar()}'.center(76))
    print(f'{amarelo()}{tracado()}{apagar()}')




