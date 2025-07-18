"""
 Índice de Massa Corporal
Receba peso e altura, calcule o IMC e apresente a classificação de acordo com o valor obtido.
"""

"""
MODULO DA LOGICA
"""
#from exercicios2.imc.interface import cabecalho

def entrada_dados(peso_entrada, altura_entrada):
    peso = float(peso_entrada.get())
    altura = float(altura_entrada.get())

    return peso, altura


def calculo_imc(peso, altura):
    imc = peso / (altura ** 2)

    return imc


def condicionais(peso_entrada, altura_entrada):
    peso, altura = entrada_dados(peso_entrada, altura_entrada)
    imc = calculo_imc(peso, altura)

    if imc <= 18.5:
        return 'abaixo do peso'
    elif 18.6 <= imc <= 24.9:
        return 'peso normal'
    elif 25 <= imc <= 29.9:
        return 'sobrepeso'
    elif imc >= 30:
        return 'obeso'




"""cabecalho()
print(condicionais())"""

