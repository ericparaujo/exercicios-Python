"""
 Índice de Massa Corporal
Receba peso e altura, calcule o IMC e apresente a classificação de acordo com o valor obtido.
"""

"""
MODULO DA LOGICA
"""
#from exercicios2.imc.interface import cabecalho
from tkinter import messagebox

def entrada_dados(peso_entrada, altura_entrada):
    peso = float(peso_entrada.get())
    altura = float(altura_entrada.get())

    return peso, altura


def calculo_imc(peso, altura):
    imc = peso / (altura ** 2)

    return imc


def condicionais(peso_entrada, altura_entrada):
    try:
        peso, altura = entrada_dados(peso_entrada, altura_entrada)
        imc = calculo_imc(peso, altura)

        if imc <= 18.5:
            return f'{imc:.2f}\n abaixo do peso'
        elif 18.6 <= imc <= 24.9:
            return f'{imc:.2f}\n peso normal'
        elif 25 <= imc <= 29.9:
            return f'{imc:.2f}\n sobrepeso'
        elif imc >= 30:
            return f'{imc:.2f}\n obeso'

    except ValueError:
        messagebox.showerror('erro', 'Valor incorreto, favor tente novamente!')




"""cabecalho()
print(condicionais())"""

