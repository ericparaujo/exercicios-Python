"""
Exercício #09 – Tabuada: elabore um programa que leia um número inteiro e mostre sua tabuada completa de 1 a 10
"""

def tabuada():
    numero = float(input('entre com o numero a ser multiplicado: '))
    for contador in range(1, 11):
        print(f'{numero} x {contador} = {numero * contador}')


tabuada()