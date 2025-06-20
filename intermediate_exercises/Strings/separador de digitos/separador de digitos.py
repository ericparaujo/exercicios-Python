"""
 Separando dígitos de um número: desenvolva um programa que leia um número de 0 a 9999 e mostre separadamente cada dígito (unidades, dezenas, centenas e milhares)
"""

def separar_digitos(numero: int) -> dict:

    if not 0 <= numero <= 999999999:
        raise ValueError('O numero deve está entre 0 e 999.999.999')

    return {'Unidade': (numero // 1) % 10,
            'Dezena': (numero // 10) % 10,
            'Centena': (numero // 100) % 10,
            'Unidade de milhar': (numero // 1000) % 10,
            'Dezena de milhar': (numero // 10000) % 10,
            'Centena de milhar': (numero // 100000) % 10,
            'Unidade de milhao': (numero // 1000000) %10,
            'Dezena de milhao': (numero // 10000000) %10,
            'Centena de milhao': (numero // 100000000) %10}


def principal():
    try:
        entrada = int(input('digite um numero entre 0 e 999.999.999: '))
        digitos = separar_digitos(entrada)
        print(f'Unidade: {digitos['Unidade']}\n'
              f'Dezena: {digitos['Dezena']}\n'
              f'Centena: {digitos['Centena']}\n'
              f'Unidade de milhar: {digitos['Unidade de milhar']}\n'
              f'Dezena de milhar: {digitos['Dezena de milhar']}\n'
              f'Centena de milhar: {digitos['Centena de milhar']}\n'
              f'Unidade de milhao: {digitos['Unidade de milhao']}\n'
              f'Dezena de milhao: {digitos['Dezena de milhao']}\n'
              f'Centena de milhao: {digitos['Centena de milhao']}')
    except ValueError as erro:
        print(f'erro: {erro}')


if __name__ == '__main__':
    principal()
