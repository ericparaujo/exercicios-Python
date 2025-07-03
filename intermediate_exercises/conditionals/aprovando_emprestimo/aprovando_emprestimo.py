"""
 Aprovando empréstimo
Escreva um programa que leia o valor de uma casa, o salário do comprador e em quantos anos ele pretende pagar. Calcule o valor da prestação mensal e informe se o empréstimo será aprovado (prestação ≤ 30% do salário).
"""
from decorator import append

from interface import bem_vindo

def entrada_dados():
    valor_casa = float(input('Digite o valor da casa: R$ '))
    salario_comprador = float(input('Digite o salario do comprador: R$ '))
    parcelas = float(input('Digite o numero de parcelas: '))
    return valor_casa, salario_comprador, parcelas


def calculo_prestacoes():
    valor_casa, salario_comprador, parcelas = entrada_dados()
    prestacoes = valor_casa / parcelas

