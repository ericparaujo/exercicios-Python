"""
MODULO DE ESTILIZACAO
"""

def configurar_fontes():
    return {
        'titulo':('arial', 16, 'bold'),
        'texto':('arial', 12, 'bold'),
        'dados':('arial', 16),
        'resultado':('arial', 18, 'bold')

    }


def exibir_texto():
    return{
        'titulo':'\n\nVAMOS VER SEU INDICE DE MASSA CORPOREA?'.center(50),
        'peso':'Qual o seu peso: ',
        'altura':'Qual sua altura: ',
        'resultado':'Seu indice IMC é:'
    }

