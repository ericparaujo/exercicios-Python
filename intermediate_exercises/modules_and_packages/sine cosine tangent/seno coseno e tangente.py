"""
Seno, cosseno e tangente: elabore um programa que leia um ângulo em graus e mostre o seno, cosseno e tangente desse ângulo
"""

from math import radians, sin, cos, tan

def angulos():
    angulo = float(input('digite o valor do angulo: '))
    print(f'o valor do seno é {sin(radians(angulo)):.2f}\n'
          f'o valor do coseno é {cos(radians(angulo)):.2f}\n'
          f'o valor da tangente é {tan(radians(angulo)):.2f}')


if __name__ == '__main__':
    angulos()
