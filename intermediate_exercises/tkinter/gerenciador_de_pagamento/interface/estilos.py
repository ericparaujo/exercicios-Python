"""
Estilos e mensagens de erro
"""
def estilos_fontes() -> dict:
    """
    estilizaçao das fontes da janela
    :return: retorna um dicionario onde o tamanho e a fonte podem ser
    reutilizados em outras partes da janela.
    """
    return {
        'titulo':('arial', 18, 'bold'),
        'texto1':('arial', 14, 'bold'),
        'texto2':('arial', 14),
        'botao':('arial', 16, 'bold'),
        'resultado':('arial', 20, 'bold')
    }


def exibir_textos():
    """
    texto usado nas janelas.
    :return: retorna os textos utilizados nos campos da janela e no botao.
    """
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
    return ['Digite o valor do produto',
            'O valor precisa ser maior que zero',
            'Digite apenas numeros inteiros ou decimais',
            'Selecione a forma de pagamento']
