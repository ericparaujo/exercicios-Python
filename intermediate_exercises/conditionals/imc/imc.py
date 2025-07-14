"""
 Índice de Massa Corporal
Receba peso e altura, calcule o IMC e apresente a classificação de acordo com o valor obtido.
"""

def entrada_dados():
    peso = float(input('Qual seu peso: '))
    altura = float(input('qual sua altura: '))

    return peso, altura


def calculo_imc(peso, altura):
    imc = peso / (altura ** 2)

    return imc


 def condicionais(imc):
     if imc <= 18.5:
         return 'abaixo do peso'
     elif 18.6 >= imc >= 24.9:
         return 'peso normal'
     elif 25 >= imc >= 29.9:
         return 'sobrepeso'
     elif imc >= 30:
         return 'obeso'




calculo_imc(*entrada_dados())
