"""
Verificando as primeiras letras de um texto: crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome “Santo”
"""

def principal():
    nome = str(input('Digite o nome completo: ')).strip().upper()
    verificar = str(input('O que deseja verificar: ')).strip().upper()
    if verificar in nome:
        print('contem palavra')
    else:
        print('nao contem palavra')


if __name__ == '__main__':
    principal()
