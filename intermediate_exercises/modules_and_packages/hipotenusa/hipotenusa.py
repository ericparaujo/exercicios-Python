"""
Catetos e hipotenusa: desenvolva um programa que leia os comprimentos dos catetos de um
triângulo retângulo e calcule a hipotenusa usando o Teorema de Pitágoras
"""

from math import hypot

def hipotenusa():
    cateto_oposto = float(input('digite o valor do cateto oposto: '))
    cateto_adjacente = float(input('digite o valor do cateto adjacente: '))
    print(f'O valor da hipotenusa é {hypot(cateto_oposto, cateto_adjacente):.2f}')


if __name__ == '__main__':
    hipotenusa()

