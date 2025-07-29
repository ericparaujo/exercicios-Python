
def estilos_fontes():
    return {
        'titulo':('arial', 18, 'bold'),
        'texto1':('arial', 14, 'bold'),
        'texto2':('arial', 14),
        'botao':('arial', 16, 'bold'),
        'resultado':('arial', 20, 'bold')
    }


def exibir_textos():
    return{
        'titulo':'Gerenciador de pagamento'.center(50).upper(),
        'valor_produto':'Valor do produto:',
        'forma_pagamento':'Forma de pagamento:',
        'botao':'Calcular'
    }


def forma_pagamento():
    return ['pagamento a vista no dinheiro',
            'pagamento a vista no cartao',
            'pagamento parcelado no cartao [2x]',
            'pagamento parcelado no cartao [+ vezes]']

def mensagem_erro():
    return ('erro')
