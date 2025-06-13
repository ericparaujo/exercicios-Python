"""
Quebrando um número: faça um programa que leia um número e mostre na tela a sua parte inteira sem usar funções de conversão direta (use o módulo math)

"""

from math import trunc

def converter_numeros():
    meu_numero = float(input('digite um numero real: '))
    print(f'o numero inteiro de {meu_numero} é {trunc(meu_numero)}')


if __name__ == '__main__':
    converter_numeros()